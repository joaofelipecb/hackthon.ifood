import kubernetes as k8s
import os
import shutil
import subprocess
import helper

def create_jenkins_directory():
    def create_dir_if_not_exists(dir_path):
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            pass

    def change_ownership_recursive(dir_path):
        for root, dirs, files in os.walk(dir_path):
            for momo in dirs:
                os.chown(os.path.join(root, momo), user=1000, group=1000)
            for momo in files:
                os.chown(os.path.join(root, momo), user=1000, group=1000)

    dir_path = '/opt/jenkins-data'
    create_dir_if_not_exists(dir_path)
    change_ownership_recursive(dir_path)


def apply_kubernetes_jenkins(k8s_client):
    resource_files = [
            'backend/data/kubernetes/dev/jenkins-pv-volume.yaml',
            'backend/data/kubernetes/dev/jenkins-pv-claim.yaml',
            'backend/data/kubernetes/dev/jenkins-deployment.yaml',
            'backend/data/kubernetes/dev/jenkins-service.yaml',
            'backend/data/kubernetes/dev/jenkins-ingress.yaml',
                 ]
    for resource_file in resource_files:
        helper.apply_kubernetes_or_handle_error(k8s_client, resource_file)

def wait_for_jenkins_ready(k8s_client, k8s_watch, k8s_core_v1):
    print('Waiting for all be ready...')
    for event in k8s_watch.stream(
                              func=k8s_core_v1.list_namespaced_pod,
                              namespace='default',
                              label_selector='app=jenkins',
                              timeout_seconds=60
                             ):
        if event['object'].status.phase == 'Running':
            k8s_watch.stop()
            return


def main():
    k8s.config.load_kube_config()
    with k8s.client.ApiClient() as k8s_client:
        k8s_watch = k8s.watch.Watch()
        k8s_core_v1 = k8s.client.CoreV1Api(k8s_client)

        create_jenkins_directory()
        apply_kubernetes_jenkins(k8s_client)
        wait_for_jenkins_ready(k8s_client, k8s_watch, k8s_core_v1)


if __name__ == '__main__':
    main()
