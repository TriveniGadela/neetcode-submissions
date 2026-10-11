class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for token in tokens:

            if token not in ["+", "-", "*", "/"]:
                st.append(int(token))

            else:
                t1 = st.pop()
                t2 = st.pop()

                if token == "+":
                    st.append(t2 + t1)

                elif token == "-":
                    st.append(t2 - t1)

                elif token == "*":
                    st.append(t2 * t1)

                elif token == "/":
                    st.append(int(t2 / t1))

        return st[0]