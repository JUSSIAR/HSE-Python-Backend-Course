const addArticle = document.getElementById("add-article")

const titleInput = document.getElementById("title")
const textInput = document.getElementById("text")
const authorInput = document.getElementById("author")


addArticle.addEventListener('click', (e) => {
    e.preventDefault()
    e.stopPropagation()

    const title = titleInput.value
    const text = textInput.value
    const author = authorInput.value

    if (!title) {
        alert("Заполните title")
        return
    }

    if (!text) {
        alert("Заполните text")
        return
    }

    if (!author) {
        alert("Заполните author")
        return
    }

    console.log("Started send data")
    fetch("http://localhost:8000/api/v1/articles/", {
        method: "POST",
        body: JSON.stringify({
            title,
            text,
            author,
        }),
        headers: {
            "Content-Type": "application/json",
            // "X-CSRFToken": '',
            mode: 'same-origin'
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
