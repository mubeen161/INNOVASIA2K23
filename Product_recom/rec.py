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
            "photo_url": "https://rukminim2.flixcart.com/image/416/416/l08gsy80/toothbrush/l/z/p/natural-herbal-miswak-sticks-pack-of-5-soft-toothbrush-5-original-imagc2tzd4dsfds5.jpeg?q=70",
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
            "photo_url": "data:image/jpeg;base64,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",
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
            "photo_url": "https://m.media-amazon.com/images/I/81Q20vMYDoL.jpg",
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

def recommendation_box(product_name, photo_url, product_link, benefits):
    # Add padding to create gaps between products
    st.write("")  # You can adjust the number of empty lines for desired spacing
    
    # Set a fixed size for the images
    image_size = (250, 250)

    st.image(photo_url, width=image_size[0])
    st.markdown(f"**[{product_name}]({product_link})**")
    st.markdown("**Benefits:**")
    for benefit in benefits:
        st.markdown(f"- {benefit}")


def main():
    st.title("Eco-Friendly and Healthy Recommendations")

    # Create a 1x3 grid layout with gaps
    col1, gap, col2, gap2, col3 = st.columns([1, 0.1, 1, 0.1, 1])

    # Random Recommendation 1
    with col1:
        random_product_1 = get_random_product()
        recommendation_box(**random_product_1)

    # Gap between columns
    with gap:
        st.write("")

    # Random Recommendation 2
    with col2:
        random_product_2 = get_random_product([random_product_1])
        recommendation_box(**random_product_2)

    # Gap between columns
    with gap2:
        st.write("")

    # Random Recommendation 3
    with col3:
        random_product_3 = get_random_product([random_product_1, random_product_2])
        recommendation_box(**random_product_3)

if __name__ == "__main__":
    main()