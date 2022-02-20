Table recipe {
  id int [pk]
  name varchar [not null]
  description text
}

Table ingredient {
  id int [pk]
  name varchar [not null, unique]
}

Table ingredient_x_recipe {
  id int [pk]
  recipe_id int [ref: > recipe.id, not null]
  ingredient_id int [ref: > recipe.id, not null]
  amount float [not null]
  amount_unit varchar [not null]
}

Table grocery {
  id int [pk]
  name varchar [not null]
  shipping_cost float [not null]
  shipping_cost_distance_unit varchar [not null]
  shipping_cost_currency_unit varchar [not null]
  geolocalization_latitude float [not null]
  geolocalization_longitude float [not null]
}

Table product {
  id int [pk]
  name varchar [not null]
  image varchar [not null]
  amount float [not null]
  amount_unit varchar [not null]
  vegetarian bool [not null]
  vegan bool [not null]
  diet bool [not null]
  light bool [not null]
  lactose_free bool [not null]
  gluten_free bool [not null]
}

Table product_x_grocery {
  id int [pk]
  product_id int [ref: > product.id, not null]
  grocery_id int [ref: > grocery.id, not null]
  price float [not null]
  price_currency_unit varchar [not null]
}

Table customer{
  id int [pk]
  name varchar [not null]
}

Table ai_weight_customer {
  id int [pk]
  customer_id int [ref: > customer.id, not null]
  lowest_total_price float [not null]
  best_cost_benefit float [not null]
  lower_time_to_ship float [not null]
}

Table ai_weight_default {
  id int [pk]
  lowest_total_price float [not null]
  best_cost_benefit float [not null]
  lowest_time_to_ship float [not null]
}

Table ai_similarity_ingredient_x_product_customer {
  id int [pk]
  customer_id int [ref: > customer.id, not null]
  ingredient_id int [ref: > ingredient.id, not null]
  product_id int [ref: > product.id, not null]
  score float [not null]
}

Table ai_similarity_ingredient_x_product_default {
  id int [pk]
  ingredient_id int [ref: > ingredient.id, not null]
  product_id int [ref: > product.id, not null]
  score float [not null]
}
