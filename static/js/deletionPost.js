function deletePost(postId) {
    let postConfirmDeletion = confirm("Are you sure you want to delete the" + " post?");

    if (postConfirmDeletion) {
        $.ajax({
            url: 'posts/' + postId + '/delete',
            type: 'POST',
            headers: {'X-CSRFToken': csrftoken},
            success: function (data, textStatus, xhr) {
                if (xhr.status == 200) {
                    window.location.reload()
                }
            }
        });
    }
}
