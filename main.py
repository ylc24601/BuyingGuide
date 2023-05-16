import pandas as pd
import streamlit as st


def BuyingGuide(total_budget, spread, *prices):
    item_num = []
    for x in range(len(prices)):
        max_x = total_budget // prices[x]
        item_num.append(range(max_x + 1))
    pools = map(tuple, item_num)
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    output = []
    for prod in result:
        price_diff = total_budget - sum(map(lambda x, y: x * y, prod, prices))
        if abs(price_diff) <= spread:
            output.append((prices, prod, price_diff))
    return output


def main():
    st.title("Buying Guide")
    st.markdown("使用說明: 建議先將確定數量或單價較高的品項扣除，較不重要的次品項再以此程式計算之")
    st.warning("總金額與單價數值勿相差過大，否則將大幅增加計算時間!")
    total_budget = st.number_input("Total Budget (總預算)", value=300)
    spread = st.number_input("Spread (與預算差額)", min_value=0)
    prices = st.text_input("Prices (物品單價，以逗點分隔)", "52, 39, 45, 17, 44")
    prices = [int(price.strip()) for price in prices.split(",")]

    if st.button("Calculate"):
        results = BuyingGuide(total_budget, spread, *prices)
        if results:
            st.write("Results:")
            df = pd.DataFrame(results, columns=["Prices", "Quantity", "Price Difference"])
            st.dataframe(df)
        else:
            st.write("No results found.")


if __name__ == "__main__":
    main()
