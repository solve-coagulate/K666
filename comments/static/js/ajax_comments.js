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

function edit(comment_id) {
    if (!comment_id) {
        comment_id="";
    };
    reply_preview = document.getElementById("comment-preview-" + comment_id);
    textarea = document.getElementById("comment-textbox-" + comment_id);
    textarea.parentNode.classList.remove("hidden");
    preview_button = document.getElementById("comment-preview-button-" + comment_id);
    post_button = document.getElementById("comment-post-button-" + comment_id);
    edit_button = document.getElementById("comment-edit-button-" + comment_id);

    textarea.classList.remove("hidden");
    preview_button.classList.remove("hidden");
    post_button.classList.remove("hidden");
    reply_preview.classList.add("hidden");
    edit_button.classList.add("hidden");
    
    return false;
}

function post(comment_id) {
    if (!comment_id) {
        comment_id="";
    };
    reply_preview = document.getElementById("comment-preview-" + comment_id);
    new_comments = document.getElementById("new-comments-" + comment_id);
    new_comment = document.createElement("div");
    $(new_comments).after(new_comment);
    // new_comments.insertBefore(new_comment, new_comments.childNodes[0]);
    new_comment.innerHTML = "Posting New Comment...";
    new_comment.classList.remove("hidden");
    
    textarea = document.getElementById("comment-textbox-" + comment_id);
    preview_button = document.getElementById("comment-preview-button-" + comment_id);
    post_button = document.getElementById("comment-post-button-" + comment_id);
    edit_button = document.getElementById("comment-edit-button-" + comment_id);
    // alert(textarea.value);
    // return false;
    text = textarea.value;    
    // if (!text) text = textarea.val();
    
    $.ajax({
        url : "/comments/ajax_add.html",
        type : "POST",
        data : { comment_text : text, parent_comment_id : comment_id },
        // handle success response
        success : function(json) {
            new_comment.innerHTML = json.html;
            textarea.value = "";

            if (comment_id) {
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
