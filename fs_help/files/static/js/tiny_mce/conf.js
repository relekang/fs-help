$().ready(function() {
    $('textarea').tinymce({
        script_url : '/static/js/tiny_mce/tiny_mce.js',
        content_css : '/static/tiny_mce.css',
        theme : "advanced",
        plugins : "spellchecker,preview",

        // Theme options - button# indicated the row# only
        theme_advanced_buttons1 : "bold,italic,underline,forecolor,|,justifyleft,justifycenter,justifyright,|,sub,sup,formatselect|,bullist,numlist,|,outdent,indent,|,undo,redo,|,link,unlink,anchor,image,|,code,preview,",
        theme_advanced_buttons2 : "",
        theme_advanced_buttons3 : "",
        theme_advanced_toolbar_location : "top",
        theme_advanced_resizing : true,
        theme_advanced_statusbar_location : "bottom",
        valid_styles : { '*' : 'color,font-weight,font-style,text-decoration' }
    });
});