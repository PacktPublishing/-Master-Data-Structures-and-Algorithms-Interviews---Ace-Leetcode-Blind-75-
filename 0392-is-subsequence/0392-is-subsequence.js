
function isSubsequence(str1, str2) {
    let itr1 = 0, itr2 = 0;

    while (itr1 < str1.length && itr2 < str2.length) {
        if (str1[itr1] === str2[itr2]) {
            itr1++;
        }
        itr2++;
    }

    return itr1 === str1.length;
}
