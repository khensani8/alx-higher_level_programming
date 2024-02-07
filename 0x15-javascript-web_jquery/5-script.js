// adds <li> element to a list when user clicks on #DIVadd_item
$(document).ready(function(){
    $("DIV#add_item").click(function(){
        $("UL.my_list").append("<li>Item</li>");
    });
});