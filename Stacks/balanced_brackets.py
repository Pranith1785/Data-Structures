
def balancedBrackets(str_bracket):

    stack = []

    l = len(str_bracket)
    if l % 2 != 0:
        return("NO")
    else:
        for val in str_bracket:
            if val == "{" or val == "(" or val == "[":
                stack.append(val)
            else:
                if len(stack) == 0:
                    return "NO"
                if (val == "}" and stack[-1] == "{") or (val == "]" and stack[-1] == "[") or (val == ")" and stack[-1] == "("):
                    stack.pop()
                else:
                    return "NO"
        if len(stack) > 0:
            return "NO"
        else:
            return("YES")


print(balancedBrackets("{(([])[])[]}"))
print(balancedBrackets("{(([])[])[]]}"))
print(balancedBrackets("{(([]){][])[]]}"))
