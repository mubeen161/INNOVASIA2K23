import streamlit as st
import random

def get_random_product(previous_products=[]):
    products = [
        {
            "product_name": "Product A",
            "photo_url": "https://via.placeholder.com/150",
            "benefits": [
                "Benefit 1",
                "Benefit 2",
                "Benefit 3",
            ],
        },
        {
            "product_name": "Product B",
            "photo_url": "https://via.placeholder.com/150",
            "benefits": [
                "Benefit 1",
                "Benefit 2",
                "Benefit 3",
            ],
        },
        {
            "product_name": "Product C",
            "photo_url": "https://via.placeholder.com/150",
            "benefits": [
                "Benefit 1",
                "Benefit 2",
                "Benefit 3",
            ],
        },
        {
            "product_name": "Product D",
            "photo_url": "https://via.placeholder.com/150",
            "benefits": [
                "Benefit 1",
                "Benefit 2",
                "Benefit 3",
            ],
        },
        {
            "product_name": "Product E",
            "photo_url": "https://via.placeholder.com/150",
            "benefits": [
                "Benefit 1",
                "Benefit 2",
                "Benefit 3",
            ],
        },
    ]

    # Exclude previously shown products
    available_products = [product for product in products if product not in previous_products]

    # If all products have been shown, reset the list
    if not available_products:
        available_products = products

    return random.choice(available_products)

def recommendation_grid(product_name, photo_url, benefits):
    st.image(photo_url, width=150)
    st.markdown(f"**{product_name}**")
    st.markdown("**Benefits:**")
    for benefit in benefits:
        st.markdown(f"- {benefit}")

def main():
    st.title("Product Recommendations")

    # Create a 5x1 grid layout with gaps
    col1, col2, col3, col4, col5 = st.columns(5)

    # Random Recommendation 1
    with col1:
        random_product_1 = get_random_product()
        recommendation_grid(**random_product_1)

    # Separator line
    st.markdown("***")

    # Random Recommendation 2
    with col2:
        random_product_2 = get_random_product([random_product_1])
        recommendation_grid(**random_product_2)

    # Separator line
    st.markdown("***")

    # Random Recommendation 3
    with col3:
        random_product_3 = get_random_product([random_product_1, random_product_2])
        recommendation_grid(**random_product_3)

    # Separator line
    st.markdown("***")

    # Random Recommendation 4
    with col4:
        random_product_4 = get_random_product([random_product_1, random_product_2, random_product_3])
        recommendation_grid(**random_product_4)

    # Separator line
    st.markdown("***")

    # Random Recommendation 5
    with col5:
        random_product_5 = get_random_product([random_product_1, random_product_2, random_product_3, random_product_4])
        recommendation_grid(**random_product_5)

if __name__ == "__main__":
    main()
