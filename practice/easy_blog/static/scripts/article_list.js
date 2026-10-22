const articlesList = document.getElementById("list")

function mapArticleToHtml(article) {
    return `<li>
        <div>
            <b>Id</b>: ${article.id}
        </div>
        <div>
            <b>Title</b>: ${article.title}
        </div>
        <div>
            <b>Text</b>: ${article.text}
        </div>
        <div>
            <b>Author</b>: ${article.author || '-----'}
        </div>
    </li>`
}

fetch("http://localhost:8000/api/v1/articles/")
    .then(data => data.json())
    .then(data => {
        const rendered = data
            .map(item => mapArticleToHtml(item))
            .join('')
        articlesList.innerHTML = `<ul>${rendered}</ul>`
    })