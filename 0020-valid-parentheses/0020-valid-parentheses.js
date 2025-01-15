
function isValid(s) {
    const stack = [];
    const bracketMap = {
        ')': '(',
        ']': '[',
        '}': '{'
    };

    for (let char of s) {
        if (bracketMap[char]) {
            if (stack.length > 0 && stack[stack.length - 1] === bracketMap[char]) {
                stack.pop();
            } else {
                return false;
            }
        } else {
            stack.push(char);
        }
    }

    return stack.length === 0;
}
