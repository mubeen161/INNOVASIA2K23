import streamlit as st
import random

def get_random_product(previous_products=[]):
    products = [
        {
            "product_name": "Organic Herbal Tea",
            "photo_url": "https://m.media-amazon.com/images/I/71hRQpIAEGL._SX679_.jpg",
            "product_link": "https://www.amazon.in/Onlyleaf-Chamomile-Green-Exotic-Samples/dp/B07D9W9H5P/ref=sr_1_8?qid=1701459324&refinements=p_n_feature_browse-bin%3A4868053031&s=grocery&sr=1-8",
            "benefits": [
                "Antioxidant-rich for overall health.",
                "Calms and reduces stress naturally.",
                "Aids digestion and soothes stomach.",
            ],
        },
        {
            "product_name": "Disposable Wooden Forks",
            "photo_url": "https://m.media-amazon.com/images/I/41ZWRcBDOEL._SX300_SY300_QL70_FMwebp_.jpg",
            "product_link": "https://www.amazon.in/Time-Disposable-Wooden-Cutlery-Eco-Friendly/dp/B09Z2ZHJWN/ref=sr_1_5?keywords=eco%2Bfriendly%2Butensils&qid=1701459629&sr=8-5&th=1",
            "benefits": [
                "Lightweight yet sturdy for use.",
                "Natural and renewable material choice.",
                "Adds a rustic, aesthetic touch.",
            ],
        },
        {
            "product_name": "Beeswax Wraps",
            "photo_url": "https://www.urbancreative.co.in/wp-content/uploads/2021/03/dsc-1.jpg",
            "product_link": "https://www.urbancreative.co.in/beeswax-food-wraps/",
            "benefits": [
                "Eco-friendly alternative to plastic.",
                "Breathable and natural food storage.",
                "Biodegradable at the end.",
            ],
        },
        {
            "product_name": "Bamboo Toothbursh",
            "photo_url": "https://brownliving.in/cdn/shop/products/bamboo-toothbrush-colour-pack-4-pcs-192-16594-colourfulpackof4-tooth-brush-brown-living-663266_800x.jpg?v=1682960582",
            "product_link": "https://bambooindia.com/collections/bamboo-brush",
            "benefits": [
                # "Eco-friendly alternative to plastic toothbrushes.",
                "Biodegradable and sustainable material choice.",
                "Renewable resource with minimal environmental impact.",
                "Naturally antimicrobial and antibacterial properties.",
        # "Reduces plastic pollution in oceans.",
            ],
        },
        {
            "product_name": "Miswak Toothbrush",
            "photo_url": "https://images.meesho.com/images/products/93608679/jnun7_512.webp",
            "product_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.meesho.com%2Fmiswak-stick-miswak-toothbrush-herbal-toothbrush-miswak-datun-pack-of-10%2Fp%2F1jqcx3&psig=AOvVaw26A98BWJuSOhrsNOBYct0D&ust=1701546662031000&source=images&cd=vfe&opi=89978449&ved=0CBQQjhxqFwoTCIDW1bSB74IDFQAAAAAdAAAAABBH",
            "benefits": [
                "Natural tooth-cleaning twig.",
        "Promotes oral hygiene and health.",
        # "Contains natural antimicrobial properties.",
        "May help prevent gum disease.",
        # "Environmentally friendly oral care choice.",
            ],
        },
        {
            "product_name": "Seed Packets",
            "photo_url": "https://m.media-amazon.com/images/I/71Edfmb50jL.jpg",
            "product_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.in%2FNavika-Seeds-Vegetable-vegetables-gardening%2Fdp%2FB09FSZYV1M&psig=AOvVaw0c_oPOYqOw1cO-RGgRv4uH&ust=1701546828316000&source=images&cd=vfe&opi=89978449&ved=0CBQQjhxqFwoTCOjSvIOC74IDFQAAAAAdAAAAABAE",
            "benefits": [
                    "Easy way to start gardening.",
                    "Includes diverse plant varieties.",
                    # "Educational for all ages.",
                    "Promotes biodiversity in gardens.",
        # "Contributes to sustainable practices.",
            ],
        },
         {
            "product_name": "Natural Candles",
            "photo_url": "https://brownliving.in/cdn/shop/articles/the-different-types-of-eco-friendly-aroma-candles-and-their-uses-958136.jpg?v=1695469368",
            "product_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fbrownliving.in%2Fblogs%2Fbrown-journal%2Fthe-different-types-of-eco-friendly-aroma-candles-and-their-uses&psig=AOvVaw0E42IyjcF7F2e0D3kct1ii&ust=1701547050244000&source=images&cd=vfe&opi=89978449&ved=0CBQQjhxqFwoTCNCXsu-C74IDFQAAAAAdAAAAABAF",
            "benefits": [
                    "Made from sustainable materials.",
        "Non-toxic and free of harmful chemicals.",
        # "Biodegradable, minimizing environmental impact.",
        "Scented with natural essential oils.",
        # "Supports eco-friendly and ethical practices.",
            ],
        },
         {
            "product_name": "Biodegradable Food Waste Bag",
            "photo_url": "https://m.media-amazon.com/images/I/71gV3XfVPbL._AC_UF1000,1000_QL80_.jpg",
            "product_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.amazon.in%2FBiodegradable-Garbage-Wastebasket-Compostable-Bathroom%2Fdp%2FB09YNNJFG3&psig=AOvVaw1ss7uzpLIYwZ8Tjf80E_XD&ust=1701547423779000&source=images&cd=vfe&opi=89978449&ved=0CBQQjhxqFwoTCPiJr6CE74IDFQAAAAAdAAAAABAL",
            "benefits": [
                    # "Eco-friendly alternative to plastic bags.",
                    "Break down naturally, reducing landfill waste.",
                    "Made from renewable and sustainable resources.",
                    "Helps minimize environmental impact.",
                    # "Suitable for composting organic waste.",
            ],
        },
         {
            "product_name": "Pot Plants",
            "photo_url": "https://www.ikea.com/in/en/images/products/fejka-artifi-potted-plant-w-pot-set-of-3-in-outdoor-herbs__1034044_pe840155_s5.jpg?f=s",
            "product_link": "https://www.ikea.com/in/en/p/fejka-artifi-potted-plant-w-pot-set-of-3-in-outdoor-herbs-80508405/?utm_source=google&utm_medium=surfaces&utm_campaign=shopping_feed&utm_content=free_google_shopping_clicks_Decoration",
            "benefits": [
                #    "Enhance indoor and outdoor spaces.",
                    "Improve air quality by oxygenating.",
                    # "Promote relaxation and stress reduction.",
                    "Create a connection with nature.",
                    "Encourage mindfulness and well-being.",
            ],
        },
      
    ]

    # Exclude previously shown products
    available_products = [product for product in products if product not in previous_products]

    # If all products have been shown, reset the list
    if not available_products:
        available_products = products

    return random.choice(available_products)

def recommendation_grid(product_name, photo_url, description, benefits):
    st.image(photo_url, width=150)
    st.markdown(f"**{product_name}**")
    st.write(description)
    st.markdown("**Benefits:**")
    for benefit in benefits:
        st.markdown(f"- {benefit}")

def main():
    st.title("Product Recommendations")

    # Create a 1x5 grid layout
    col1, col2, col3, col4, col5 = st.columns(5)

    # Random Recommendation 1
    with col1:
        random_product_1 = get_random_product()
        recommendation_grid(**random_product_1)

    # Random Recommendation 2
    with col2:
        random_product_2 = get_random_product([random_product_1])
        recommendation_grid(**random_product_2)

    # Random Recommendation 3
    with col3:
        random_product_3 = get_random_product([random_product_1, random_product_2])
        recommendation_grid(**random_product_3)

    # Random Recommendation 4
    with col4:
        random_product_4 = get_random_product([random_product_1, random_product_2, random_product_3])
        recommendation_grid(**random_product_4)

    # Random Recommendation 5
    with col5:
        random_product_5 = get_random_product([random_product_1, random_product_2, random_product_3, random_product_4])
        recommendation_grid(**random_product_5)

if __name__ == "__main__":
    main()
