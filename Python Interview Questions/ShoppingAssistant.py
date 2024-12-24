class User:
    def __init__(self, user_id, name, preferences, budget):
        self.user_id = user_id
        self.name = name
        self.preferences = preferences
        self.budget = budget

class Product:
    def __init__(self, product_id, name, category, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price

class ShoppingAssistant:
    def __init__(self):
        self.products = []  # A list to store available products
        self.user_shopping_cart = {}  # Stores user-specific shopping carts

    def add_product(self, product):
        self.products.append(product)

    def recommend_products(self, user):
        """Recommend products based on the user's preferences and budget."""
        recommendations = []
        for product in self.products:
            if product.category in user.preferences and product.price <= user.budget:
                recommendations.append(product)
        return recommendations

    def add_to_cart(self, user, product_id):
        """Add a product to the user's shopping cart if it fits within their budget."""
        if user.user_id not in self.user_shopping_cart:
            self.user_shopping_cart[user.user_id] = []

        product = next((p for p in self.products if p.product_id == product_id), None)
        if product:
            if product.price <= user.budget:
                self.user_shopping_cart[user.user_id].append(product)
                user.budget -= product.price
                return f"Added {product.name} to {user.name}'s cart. Remaining budget: {user.budget}"
            else:
                return f"{product.name} exceeds the remaining budget."
        else:
            return "Product not found."

    def view_cart(self, user):
        """View the user's shopping cart."""
        return self.user_shopping_cart.get(user.user_id, [])

    def personalized_deals(self, user):
        """Generate personalized deals based on the user's purchase history."""
        # Simplified: Recommend cheaper alternatives in the same category
        purchased_categories = {product.category for product in self.user_shopping_cart.get(user.user_id, [])}
        deals = []
        for product in self.products:
            if product.category in purchased_categories and product.price < user.budget:
                deals.append(product)
        return deals

    def spending_insights(self, user):
        """Provide insights on total spending and savings."""
        cart = self.user_shopping_cart.get(user.user_id, [])
        total_spent = sum(product.price for product in cart)
        savings = user.budget  # Remaining budget represents savings
        return {
            "Total Spent": total_spent,
            "Savings": savings
        }


# Example Usage
user = User(user_id=1, name="Alice", preferences=["Electronics", "Clothing"], budget=500)

assistant = ShoppingAssistant()

# Adding products
assistant.add_product(Product(1, "Smartphone", "Electronics", 300))
assistant.add_product(Product(2, "T-Shirt", "Clothing", 50))
assistant.add_product(Product(3, "Headphones", "Electronics", 100))
assistant.add_product(Product(4, "Jacket", "Clothing", 200))

# Recommend products
recommendations = assistant.recommend_products(user)
print("\nRecommended Products:")
for product in recommendations:
    print(f"Product ID: {product.product_id}, Name: {product.name}, Category: {product.category}, Price: ${product.price}")

# Add to cart
print("\n" + assistant.add_to_cart(user, 1))
print(assistant.add_to_cart(user, 2))

# View cart
print("\nShopping Cart:")
cart = assistant.view_cart(user)
for item in cart:
    print(f"Product ID: {item.product_id}, Name: {item.name}, Category: {item.category}, Price: ${item.price}")

# Personalized deals
print("\nPersonalized Deals:")
deals = assistant.personalized_deals(user)
for deal in deals:
    print(f"Product ID: {deal.product_id}, Name: {deal.name}, Category: {deal.category}, Price: ${deal.price}")

# Spending insights
insights = assistant.spending_insights(user)
print("\nSpending Insights:")
for key, value in insights.items():
    print(f"{key}: ${value}")
