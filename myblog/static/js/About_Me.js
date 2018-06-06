/**
 * Created by H on 2018/6/2.
 */
// coding：utf8

// 弹出隐藏层
function OpenDiv(show_div,bg_div) {
    document.getElementById(show_div).style.display='block';
    document.getElementById(bg_div).style.display='block';
    var bg_id=document.getElementById(bg_div);
    bg_id.style.width=document.body.scrollWidth;
    bg_id.style.height=$(document).height();
    $("#"+bg_div).height($(document).height());
}

// 关闭隐藏层
function CloseDiv(show_div,bg_div) {
    document.getElementById(show_div).style.display='none';
    document.getElementById(bg_div).style.display='none';

 }