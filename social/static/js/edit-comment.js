function viewEditCommentForm(csrf, commentId, comment){
    const commentEdit = document.getElementById(`edit-comment-${commentId}`)
    const textArea = document.createElement('div')
    textArea.innerHTML = `<form id="edit-comment-${commentId}" method="POST" action="/comments/edit/${commentId}">
      ${csrf}
      <input value="${comment}" type="text" name="content" style="width: 400px; height: 60px;">
      <button>Edit</button>
    </form>`
    const child = commentEdit.children[0]
    commentEdit.replaceChild(textArea, child)
}