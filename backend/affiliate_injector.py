def add_affiliate_links(ai_text):
    if "protein" in ai_text.lower():
        ai_text += "\n\n💪 Recommended Product: [Optimum Nutrition Protein](https://amzn.to/YOUR_AMAZON_ID)"
    if "laptop" in ai_text.lower():
        ai_text += "\n\n💻 Check this out: [HP Laptop](https://amzn.to/YOUR_AMAZON_ID)"
    return ai_text