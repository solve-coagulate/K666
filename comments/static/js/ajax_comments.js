function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^GET|HEAD|OPTIONS|TRACE$/.test(settings.type)) && !this.crossDomain) {
            xhr.setRequestHeader('X-CSRFToken', csrftoken);
        }
    }
});

function ajax_preview(comment_id) {
    if (!comment_id) {
        comment_id="";
    };
    reply_preview = document.getElementById("comment-preview-" + comment_id);
    reply_preview.innerHTML = "Fetching Preview...";
    reply_preview.classList.remove("hidden");

    textarea = document.getElementById("comment-textbox-" + comment_id);
    preview_button = document.getElementById("comment-preview-button-" + comment_id);
    post_button = document.getElementById("comment-post-button-" + comment_id);
    edit_button = document.getElementById("comment-edit-button-" + comment_id);
    // alert(textarea.value);
    // return false;
    text = textarea.value;    
    // if (!text) text = textarea.val();
    
    $.ajax({
        url : "/comments/ajax_preview.html",
        type : "POST",
        data : { comment_text : text, parent_comment_id : comment_id },
        // handle success response
        success : function(json) {
            reply_preview.innerHTML = json.html;
            textarea.classList.add("hidden");
            preview_button.classList.add("hidden");
            post_button.classList.remove("hidden");
            edit_button.classList.remove("hidden");
            // textarea.focus();
            // alert(json.markdown);
            return false;
        },
        error : function(xhr, status, error) {
            // alert(xhr.responseText)
            reply_preview.innerHTML = "PREVIEW FAILURE: " + status + " " + error  + "<pre>" + xhr.responseText + "</pre>";
            // textarea.focus();
        },
    });
    
    return false;
}

function ajax_reply(comment_parent_id) {
    
    textarea = document.getElementById("comment-textbox-" + comment_parent_id);    
    if (textarea != null) {
        return edit(comment_parent_id);
    };
    
    reply_form = document.getElementById("reply-form-" + comment_parent_id);
    reply_form.classList.remove("hidden");

    $.ajax({
        url : "/comments/ajax_comment_form.html",
        type : "POST",
        data : { comment_text : "", parent_comment_id : comment_parent_id },
        // handle success response
        success : function(json) {
            reply_form.innerHTML = "" + json.html;
            // reply_preview.innerHTML = json.html;
            // textarea.classList.add("hidden");
            // preview_button.classList.add("hidden");
            // post_button.classList.remove("hidden");
            // edit_button.classList.remove("hidden");
            // textarea.focus();
            // alert(json.markdown);
            return false;
        },
        error : function(xhr, status, error) {
            // alert(xhr.responseText);
            // reply_form.innerHTML = "WHOOOHOOO"; 
            reply_form.innerHTML = "PREVIEW FAILURE: " + status + " " + error  + "<pre>" + xhr.responseText + "</pre>";
            // reply_preview.innerHTML = "PREVIEW FAILURE: " + status + " " + error  + "<pre>" + xhr.responseText + "</pre>";
            // textarea.focus();
            return false;
        },
    });

    return false;

};

function edit(comment_parent_id) {
    if (!comment_parent_id) {
        comment_parent_id="";
    };
    
    reply_form = document.getElementById("reply-form-" + comment_parent_id);
    reply_form.classList.remove("hidden");

    reply_preview = document.getElementById("comment-preview-" + comment_parent_id);
    textarea = document.getElementById("comment-textbox-" + comment_parent_id);
    textarea.parentNode.classList.remove("hidden");
    preview_button = document.getElementById("comment-preview-button-" + comment_parent_id);
    post_button = document.getElementById("comment-post-button-" + comment_parent_id);
    edit_button = document.getElementById("comment-edit-button-" + comment_parent_id);

    textarea.classList.remove("hidden");
    preview_button.classList.remove("hidden");
    post_button.classList.remove("hidden");
    reply_preview.classList.add("hidden");
    edit_button.classList.add("hidden");
    
    return false;
}

function ajax_post(comment_parent_id) {
    if (!comment_parent_id) {
        comment_parent_id="";
    };
    
    reply_preview = document.getElementById("comment-preview-" + comment_parent_id);
    new_comments = document.getElementById("new-comments-" + comment_parent_id);
    new_comment = document.createElement("div");
    $(new_comments).after(new_comment);
    // new_comments.insertBefore(new_comment, new_comments.childNodes[0]);
    new_comment.innerHTML = "Posting New Comment...";
    new_comment.classList.remove("hidden");
    
    textarea = document.getElementById("comment-textbox-" + comment_parent_id);


    preview_button = document.getElementById("comment-preview-button-" + comment_parent_id);
    post_button = document.getElementById("comment-post-button-" + comment_parent_id);

    edit_button = document.getElementById("comment-edit-button-" + comment_parent_id);
    // alert(comment_parent_id);
    // alert(textarea);
    // return false;
    text = textarea.value;    
    // if (!text) text = textarea.val();
    
    // alert(comment_parent_id);

    $.ajax({
        url : "/comments/ajax_add.html",
        type : "POST",
        data : { comment_text : text, parent_comment_id : comment_parent_id },
        // handle success response
        success : function(json) {
            new_comment.innerHTML = json.html;
            textarea.value = "";

            if (comment_parent_id) {
                textarea.parentNode.classList.add("hidden");
            };
                                
            textarea.classList.remove("hidden");
            preview_button.classList.remove("hidden");
            post_button.classList.remove("hidden");
            reply_preview.classList.add("hidden");
            edit_button.classList.add("hidden");
            // textarea.focus();
            // alert(json.markdown);
            return false;
        },
        error : function(xhr, status, error) {
            // alert(xhr.responseText)
            new_comment.innerHTML = "COMMENT POSTING FAILURE: " + status + " " + error + "<pre>" + xhr.responseText + "</pre>";
            // textarea.focus();
        },
    });
    
    return false;
}
