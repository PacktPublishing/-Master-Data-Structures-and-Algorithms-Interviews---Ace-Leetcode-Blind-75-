function numRescueBoats(people, limit) {
    people.sort((a, b) => a - b);
    let i = 0;
    let j = people.length - 1;
    let boats = 0;

    while (i <= j) {
        boats++;
        if (people[i] + people[j] <= limit) {
            i++;
        }
        j--;
    }

    return boats;
}