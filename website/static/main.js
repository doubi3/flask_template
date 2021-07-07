function deleteBlog(blogId) {
    fetch('/delete-blog', {
        method: 'POST',
        body: JSON.stringify({ blogId: blogId })
    }).then((_res) => {
        window.location.href = "/";
    });
}