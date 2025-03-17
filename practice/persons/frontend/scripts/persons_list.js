const personsList = document.getElementById("list")

function mapPersonToHtml(person) {
    return `<li>
        <div>
            <b>Id</b>: ${person.id}
        </div>
        <div>
            <b>first_name</b>: ${person.first_name}
        </div>
        <div>
            <b>last_name</b>: ${person.last_name}
        </div>
    </li>`
}

fetch("http://localhost:8000/api/v1/persons/")
    .then(data => data.json())
    .then(data => {
        const rendered = data.map(item => mapPersonToHtml(item)).join('')
        personsList.innerHTML = `<ul>${rendered}</ul>`
    })