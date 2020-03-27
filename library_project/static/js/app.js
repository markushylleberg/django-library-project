function checkIfStaff(event) {

    const secretField = document.getElementById('secretField');

    if (event.target.value == 'staff') {
        secretField.classList.remove('hidden');
    } else {
        secretField.classList.add('hidden');
    }
}

function checkIfBookOrMagazine(event) {
    
    const authorField = document.getElementById('authorField');

    if (event.target.value == 'book') {
        authorField.classList.remove('hidden')
    }
    else {
        authorField.classList.add('hidden')
    }
}