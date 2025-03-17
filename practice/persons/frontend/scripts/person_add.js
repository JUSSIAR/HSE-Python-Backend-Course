const addPerson = document.getElementById("add-person")

const firstNameInput = document.getElementById("first_name")
const lastNameInput = document.getElementById("last_name")



addPerson.addEventListener('click', (e) => {
    e.preventDefault()
    e.stopPropagation()

    const firstName = firstNameInput.value
    const lastName = lastNameInput.value

    if (!firstName) {
        alert("Заполните first_name")
        return
    }

    if (!lastName) {
        alert("Заполните last_name")
        return
    }

    console.log("Started send data")
    fetch("http://localhost:8000/api/v1/persons/", {
        method: "POST",
        body: JSON.stringify({
            "first_name": firstName,
            "last_name": lastName,
        }),
        headers: {
            "Content-Type": "application/json",
        }
    })
        .then(data => {
            if (!data.ok) {
                console.warn("NOT OK")
                return data
            }
            return data.json()
        })
        .then(data => alert(`Added: ${JSON.stringify(data)}`))
        .catch(err => console.error(err))
})
