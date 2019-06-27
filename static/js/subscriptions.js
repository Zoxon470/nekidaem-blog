function userSubscription(e, blogId, status) {
    if (status == 'subscribed') {
      $.ajax({
          url: blogId + '/subscribe',
          type: 'POST',
          headers: {'X-CSRFToken': csrftoken},
          dataType: 'json',
          traditional: true,
          success: function (data, textStatus, xhr) {
              if (xhr.status == 200) {
                  window.location.reload()
              }
          }
        });
    } else if (status == 'unsubscribed') {
      $.ajax({
          url: blogId + '/unsubscribe',
          type: 'POST',
          headers: {'X-CSRFToken': csrftoken},
          dataType: 'json',
          traditional: true,
          success: function (data, textStatus, xhr) {
              if (xhr.status == 200) {
                  window.location.reload()
              }
          }
      });
    }
}
