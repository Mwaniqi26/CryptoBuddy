# 🧠 CryptoBuddy – Your First AI-Powered Financial Sidekick!

# 📌 Run this cell to start chatting with CryptoBuddy

# --- Step 1: Define CryptoBuddy's Personality ---
print("👋 Hi there! I'm CryptoBuddy – your AI-powered financial sidekick! 💰")
print("Ask me anything about crypto trends and sustainability.\n")

# --- Step 2: Sample Crypto Dataset ---
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

# --- Step 3: Chatbot Logic ---
def get_recommendation(user_query):
    user_query = user_query.lower()

    # Advice based on sustainability
    if "sustainable" in user_query or "eco" in user_query or "green" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"🌱 Go for {recommend}! It’s eco-friendly with a sustainability score of {crypto_db[recommend]['sustainability_score'] * 10}/10.")

    # Advice based on price trend
    elif "trending" in user_query or "rising" in user_query or "growth" in user_query:
        options = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        if options:
            best = max(options, key=lambda x: (crypto_db[x]["market_cap"] == "high", crypto_db[x]["sustainability_score"]))
            print(f"🚀 {best} is trending up with strong growth potential!")
        else:
            print("📉 Hmm... No coins are trending up at the moment.")

    # General recommendation
    elif "long-term" in user_query or "best" in user_query:
        candidates = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising" and crypto_db[coin]["sustainability_score"] > 0.7]
        if candidates:
            best = candidates[0]
            print(f"💡 For long-term growth, consider {best}. It's rising and eco-smart! ✅")
        else:
            print("⚠️ No clear winner right now. Keep watching the market!")

    # Unknown input
    else:
        print("🤔 I'm not sure about that. Try asking me things like:")
        print("   - Which crypto is most sustainable?")
        print("   - What’s trending up?")
        print("   - What's best for long-term growth?")

    # Disclaimer
    print("\n⚠️ Disclaimer: Crypto is risky—always do your own research!")

# --- Step 4: Continuous Chat Loop ---
# Keeps running until the user types "exit", "quit", or "bye"
while True:
    query = input("\nYou: ")
    if query.lower() in ["exit", "quit", "bye"]:
        print("👋 See you soon! Stay smart and invest wisely.")
        break
    get_recommendation(query)

