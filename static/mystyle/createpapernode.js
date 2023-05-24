

function createNode(formlabel) {
    var e_0 = document.createElement("div");
    e_0.setAttribute("class", "question-group animate__animated animate__fadeIn hvr-grow-shadow");
    var e_1 = document.createElement("div");
    e_1.setAttribute("class", "display-flex");
    var e_2 = document.createElement("label");
    e_2.setAttribute("class", "form-label");
    e_2.innerText=formlabel;
    //e_2.appendChild(document.createTextNode(formlabel));
    e_1.appendChild(e_2);


    var e_mark = document.createElement("input");
    e_mark.setAttribute("id", "singlemark"+formlabel);
    e_mark.setAttribute("class", "mark");
    e_mark.setAttribute("type", "number");
    e_mark.setAttribute("min", "0");
    e_mark.setAttribute("max", "100"+formlabel);
    e_mark.setAttribute("value", "1");
    e_1.appendChild(e_mark);

    var e_3 = document.createElement("button");
    e_3.setAttribute("type", "button");
    e_3.setAttribute("style", "float: right;");
    e_3.setAttribute("class", "removeclass btn btn-danger");
    e_3.appendChild(document.createTextNode("删除"));
    e_1.appendChild(e_3);

    e_0.appendChild(e_1);
    var e_4 = document.createElement("input");
    e_4.setAttribute("type", "text");
    e_4.setAttribute("name", "ques_title");
    e_4.setAttribute("class", "form-control");
    e_4.setAttribute("id", "question_title");
    e_0.appendChild(e_4);
    var e_5 = document.createElement("div");
    e_5.setAttribute("class", "input-group mb-3");
    var e_6 = document.createElement("div");
    e_6.setAttribute("class", "btn-group");
    e_6.setAttribute("style", "width:100%");
    e_6.setAttribute("role", "group");
    e_6.setAttribute("aria-label", "Basic radio toggle button group");
    var e_7 = document.createElement("input");
    e_7.setAttribute("type", "radio");
    e_7.setAttribute("class", "btn-check");
    e_7.setAttribute("name", "btnradio"+formlabel);
    e_7.setAttribute("id", "btnradio"+(formlabel-1)*4+1);
    e_7.setAttribute("autocomplete", "off");
    e_7.setAttribute("checked", "");
    e_6.appendChild(e_7);
    var e_8 = document.createElement("label");
    e_8.setAttribute("class", "btn btn-outline-primary");
    e_8.setAttribute("for", "btnradio"+(formlabel-1)*4+1);
    e_8.appendChild(document.createTextNode("A"));
    e_6.appendChild(e_8);
    var e_9 = document.createElement("input");
    e_9.setAttribute("type", "text");
    e_9.setAttribute("class", "form-control");
    e_9.setAttribute("name", "ques_option");
    e_9.setAttribute("placeholder", "选项A");
    e_9.setAttribute("aria-label", "Server");
    e_6.appendChild(e_9);
    var e_10 = document.createElement("input");
    e_10.setAttribute("type", "radio");
    e_10.setAttribute("class", "btn-check");
    e_10.setAttribute("name", "btnradio"+formlabel);
    e_10.setAttribute("id", "btnradio"+(formlabel-1)*4+2);
    e_10.setAttribute("autocomplete", "off");
    e_6.appendChild(e_10);
    var e_11 = document.createElement("label");
    e_11.setAttribute("class", "btn btn-outline-primary");
    e_11.setAttribute("for", "btnradio"+(formlabel-1)*4+2);
    e_11.appendChild(document.createTextNode("B"));
    e_6.appendChild(e_11);
    var e_12 = document.createElement("input");
    e_12.setAttribute("type", "text");
    e_12.setAttribute("class", "form-control");
    e_12.setAttribute("name", "ques_option");
    e_12.setAttribute("placeholder", "选项B");
    e_12.setAttribute("aria-label", "Server");
    e_6.appendChild(e_12);
    var e_13 = document.createElement("input");
    e_13.setAttribute("type", "radio");
    e_13.setAttribute("class", "btn-check");
    e_13.setAttribute("name", "btnradio"+formlabel);
    e_13.setAttribute("id", "btnradio"+(formlabel-1)*4+3);
    e_13.setAttribute("autocomplete", "off");
    e_6.appendChild(e_13);
    var e_14 = document.createElement("label");
    e_14.setAttribute("class", "btn btn-outline-primary");
    e_14.setAttribute("for", "btnradio"+(formlabel-1)*4+3);
    e_14.appendChild(document.createTextNode("C"));
    e_6.appendChild(e_14);
    var e_15 = document.createElement("input");
    e_15.setAttribute("type", "text");
    e_15.setAttribute("class", "form-control");
    e_15.setAttribute("name", "ques_option");
    e_15.setAttribute("placeholder", "选项C");
    e_15.setAttribute("aria-label", "Server");
    e_6.appendChild(e_15);
    var e_16 = document.createElement("input");
    e_16.setAttribute("type", "radio");
    e_16.setAttribute("class", "btn-check");
    e_16.setAttribute("name", "btnradio"+formlabel);
    e_16.setAttribute("id", "btnradio"+(formlabel-1)*4+4);
    e_16.setAttribute("autocomplete", "off");
    e_6.appendChild(e_16);
    var e_17 = document.createElement("label");
    e_17.setAttribute("class", "btn btn-outline-primary");
    e_17.setAttribute("for", "btnradio"+(formlabel-1)*4+4);
    e_17.appendChild(document.createTextNode("D"));
    e_6.appendChild(e_17);
    var e_18 = document.createElement("input");
    e_18.setAttribute("type", "text");
    e_18.setAttribute("class", "form-control");
    e_18.setAttribute("name", "ques_option");
    e_18.setAttribute("placeholder", "选项D");
    e_18.setAttribute("aria-label", "Server");
    e_6.appendChild(e_18);
    e_5.appendChild(e_6);
    e_0.appendChild(e_5);
    return e_0;
}


function editNode(formlabel,title,checedA,optionA,checedB,optionB,checedC,optionC,checedD,optionD,mark) {
    var e_0 = document.createElement("div");
    e_0.setAttribute("class", "question-group animate__animated animate__fadeIn hvr-grow-shadow");
    var e_1 = document.createElement("div");
    e_1.setAttribute("class", "display-flex");
    var e_2 = document.createElement("label");
    e_2.setAttribute("class", "form-label");
    e_2.innerText=formlabel;
    //e_2.appendChild(document.createTextNode(formlabel));
    e_1.appendChild(e_2);
    
    var e_mark = document.createElement("input");
    e_mark.setAttribute("id", "singlemark"+formlabel);
    e_mark.setAttribute("class", "mark");
    e_mark.setAttribute("type", "number");
    e_mark.setAttribute("min", "0");
    e_mark.setAttribute("max", "100"+formlabel);
    e_mark.setAttribute("value", mark);
    e_1.appendChild(e_mark);


    var e_3 = document.createElement("button");
    e_3.setAttribute("type", "button");
    e_3.setAttribute("style", "float: right;");
    e_3.setAttribute("class", "removeclass btn btn-danger");
    e_3.appendChild(document.createTextNode("删除"));
    e_1.appendChild(e_3);
    e_0.appendChild(e_1);
    var e_4 = document.createElement("input");
    e_4.setAttribute("type", "text");
    e_4.setAttribute("name", "ques_title");
    e_4.setAttribute("class", "form-control");
    e_4.setAttribute("id", "question_title");
    e_4.value = title
    e_0.appendChild(e_4);
    var e_5 = document.createElement("div");
    e_5.setAttribute("class", "input-group mb-3");
    var e_6 = document.createElement("div");
    e_6.setAttribute("class", "btn-group");
    e_6.setAttribute("style", "width:100%");
    e_6.setAttribute("role", "group");
    e_6.setAttribute("aria-label", "Basic radio toggle button group");
    var e_7 = document.createElement("input");
    e_7.setAttribute("type", "radio");
    e_7.setAttribute("class", "btn-check");
    e_7.setAttribute("name", "btnradio"+formlabel);
    e_7.setAttribute("id", "btnradio"+(formlabel-1)*4+1);
    e_7.setAttribute("autocomplete", "off");
    if(checedA==1){
        e_7.setAttribute("checked", "true");
    }
    e_6.appendChild(e_7);
    var e_8 = document.createElement("label");
    e_8.setAttribute("class", "btn btn-outline-primary");
    e_8.setAttribute("for", "btnradio"+(formlabel-1)*4+1);
    e_8.appendChild(document.createTextNode("A"));
    e_6.appendChild(e_8);
    var e_9 = document.createElement("input");
    e_9.setAttribute("type", "text");
    e_9.setAttribute("class", "form-control");
    e_9.setAttribute("name", "ques_option");
    e_9.setAttribute("placeholder", "选项A");
    e_9.setAttribute("aria-label", "Server");
    e_9.value = optionA
    e_6.appendChild(e_9);
    var e_10 = document.createElement("input");
    e_10.setAttribute("type", "radio");
    e_10.setAttribute("class", "btn-check");
    e_10.setAttribute("name", "btnradio"+formlabel);
    e_10.setAttribute("id", "btnradio"+(formlabel-1)*4+2);
    e_10.setAttribute("autocomplete", "off");
    if(checedB==1){
        e_10.setAttribute("checked", "true");
    }
    e_6.appendChild(e_10);
    var e_11 = document.createElement("label");
    e_11.setAttribute("class", "btn btn-outline-primary");
    e_11.setAttribute("for", "btnradio"+(formlabel-1)*4+2);
    e_11.appendChild(document.createTextNode("B"));
    e_6.appendChild(e_11);
    var e_12 = document.createElement("input");
    e_12.setAttribute("type", "text");
    e_12.setAttribute("class", "form-control");
    e_12.setAttribute("name", "ques_option");
    e_12.setAttribute("placeholder", "选项B");
    e_12.setAttribute("aria-label", "Server");
    e_12.value = optionB
    e_6.appendChild(e_12);
    var e_13 = document.createElement("input");
    e_13.setAttribute("type", "radio");
    e_13.setAttribute("class", "btn-check");
    e_13.setAttribute("name", "btnradio"+formlabel);
    e_13.setAttribute("id", "btnradio"+(formlabel-1)*4+3);
    e_13.setAttribute("autocomplete", "off");
    if(checedC==1){
        e_13.setAttribute("checked", "true");
    }
    e_6.appendChild(e_13);
    var e_14 = document.createElement("label");
    e_14.setAttribute("class", "btn btn-outline-primary");
    e_14.setAttribute("for", "btnradio"+(formlabel-1)*4+3);
    e_14.appendChild(document.createTextNode("C"));
    e_6.appendChild(e_14);
    var e_15 = document.createElement("input");
    e_15.setAttribute("type", "text");
    e_15.setAttribute("class", "form-control");
    e_15.setAttribute("name", "ques_option");
    e_15.setAttribute("placeholder", "选项C");
    e_15.setAttribute("aria-label", "Server");
    e_15.value = optionC
    e_6.appendChild(e_15);
    var e_16 = document.createElement("input");
    e_16.setAttribute("type", "radio");
    e_16.setAttribute("class", "btn-check");
    e_16.setAttribute("name", "btnradio"+formlabel);
    e_16.setAttribute("id", "btnradio"+(formlabel-1)*4+4);
    e_16.setAttribute("autocomplete", "off");
    if(checedD==1){
        e_16.setAttribute("checked", "true");
    }
    e_6.appendChild(e_16);
    var e_17 = document.createElement("label");
    e_17.setAttribute("class", "btn btn-outline-primary");
    e_17.setAttribute("for", "btnradio"+(formlabel-1)*4+4);
    e_17.appendChild(document.createTextNode("D"));
    e_6.appendChild(e_17);
    var e_18 = document.createElement("input");
    e_18.setAttribute("type", "text");
    e_18.setAttribute("class", "form-control");
    e_18.setAttribute("name", "ques_option");
    e_18.setAttribute("placeholder", "选项D");
    e_18.setAttribute("aria-label", "Server");
    e_18.value = optionD
    e_6.appendChild(e_18);
    e_5.appendChild(e_6);
    e_0.appendChild(e_5);
    return e_0;
}

function createjudgeNode(formlabel) {
    var e_0 = document.createElement("div");
    e_0.setAttribute("class", "judge_question-group animate__animated animate__fadeIn hvr-grow-shadow");
    var e_1 = document.createElement("div");
    e_1.setAttribute("class", "display-flex");
    var e_2 = document.createElement("label");
    e_2.setAttribute("class", "form-label");
    e_2.appendChild(document.createTextNode(formlabel));
    e_1.appendChild(e_2);

    var e_mark = document.createElement("input");
    e_mark.setAttribute("id", "judgemark"+formlabel);
    e_mark.setAttribute("class", "mark");
    e_mark.setAttribute("type", "number");
    e_mark.setAttribute("min", "0");
    e_mark.setAttribute("max", "100"+formlabel);
    e_mark.setAttribute("value", "1");
    e_1.appendChild(e_mark);

    var e_3 = document.createElement("button");
    e_3.setAttribute("type", "button");
    e_3.setAttribute("style", "float: right;");
    e_3.setAttribute("class", "removeclass btn btn-danger");
    e_3.appendChild(document.createTextNode("删除"));
    e_1.appendChild(e_3);
    e_0.appendChild(e_1);
    var e_4 = document.createElement("input");
    e_4.setAttribute("type", "text");
    e_4.setAttribute("name", "ques_title");
    e_4.setAttribute("class", "form-control");
    e_4.setAttribute("placeholder", "题目内容");
    e_4.setAttribute("autocomplete", "off");
    e_0.appendChild(e_4);
    var e_5 = document.createElement("div");
    e_5.setAttribute("class", "input-group mb-3");
    var e_6 = document.createElement("div");
    e_6.setAttribute("class", "btn-group");
    e_6.setAttribute("style", "width:100%");
    e_6.setAttribute("role", "group");
    e_6.setAttribute("aria-label", "Basic radio toggle button group");
    var e_7 = document.createElement("input");
    e_7.setAttribute("type", "radio");
    e_7.setAttribute("class", "btn-check");
    e_7.setAttribute("name", "judgebtnradio"+formlabel);
    e_7.setAttribute("id", "judgebtnradio"+(formlabel-1)*2+1);
    e_7.setAttribute("autocomplete", "off");
    e_6.appendChild(e_7);
    var e_8 = document.createElement("label");
    e_8.setAttribute("class", "btn btn-outline-primary");
    e_8.setAttribute("for", "judgebtnradio"+(formlabel-1)*2+1);
    e_8.appendChild(document.createTextNode("正确"));
    e_6.appendChild(e_8);
    var e_9 = document.createElement("input");
    e_9.setAttribute("type", "radio");
    e_9.setAttribute("class", "btn-check");
    e_9.setAttribute("name", "judgebtnradio"+formlabel);
    e_9.setAttribute("id", "judgebtnradio"+(formlabel-1)*2+2);
    e_9.setAttribute("autocomplete", "off");
    e_6.appendChild(e_9);
    var e_10 = document.createElement("label");
    e_10.setAttribute("class", "btn btn-outline-danger");
    e_10.setAttribute("for", "judgebtnradio"+(formlabel-1)*2+2);
    e_10.appendChild(document.createTextNode("错误"));
    e_6.appendChild(e_10);
    e_5.appendChild(e_6);
    e_0.appendChild(e_5);
    return e_0;
}

function editjudgeNode(formlabel,title,checedA,checedB,mark) {
    var e_0 = document.createElement("div");
    e_0.setAttribute("class", "judge_question-group animate__animated animate__fadeIn hvr-grow-shadow");
    var e_1 = document.createElement("div");
    e_1.setAttribute("class", "display-flex");
    var e_2 = document.createElement("label");
    e_2.setAttribute("class", "form-label");
    e_2.appendChild(document.createTextNode(formlabel));
    e_1.appendChild(e_2);

    var e_mark = document.createElement("input");
    e_mark.setAttribute("id", "judgemark"+formlabel);
    e_mark.setAttribute("class", "mark");
    e_mark.setAttribute("type", "number");
    e_mark.setAttribute("min", "0");
    e_mark.setAttribute("max", "100"+formlabel);
    e_mark.setAttribute("value", mark);
    e_1.appendChild(e_mark);

    var e_3 = document.createElement("button");
    e_3.setAttribute("type", "button");
    e_3.setAttribute("style", "float: right;");
    e_3.setAttribute("class", "removeclass btn btn-danger");
    e_3.appendChild(document.createTextNode("删除"));
    e_1.appendChild(e_3);
    e_0.appendChild(e_1);
    var e_4 = document.createElement("input");
    e_4.setAttribute("type", "text");
    e_4.setAttribute("name", "ques_title");
    e_4.setAttribute("class", "form-control");
    e_4.setAttribute("placeholder", "题目内容");
    e_4.setAttribute("autocomplete", "off");
    e_4.value = title
    e_0.appendChild(e_4);
    var e_5 = document.createElement("div");
    e_5.setAttribute("class", "input-group mb-3");
    var e_6 = document.createElement("div");
    e_6.setAttribute("class", "btn-group");
    e_6.setAttribute("style", "width:100%");
    e_6.setAttribute("role", "group");
    e_6.setAttribute("aria-label", "Basic radio toggle button group");
    
    var e_7 = document.createElement("input");
    e_7.setAttribute("type", "radio");
    e_7.setAttribute("class", "btn-check");
    e_7.setAttribute("name", "judgebtnradio"+formlabel);
    e_7.setAttribute("id", "judgebtnradio"+(formlabel-1)*2+1);
    e_7.setAttribute("autocomplete", "off");
    if(checedA==1){
        e_7.setAttribute("checked", "true");
    }
    e_6.appendChild(e_7);
    var e_8 = document.createElement("label");
    e_8.setAttribute("class", "btn btn-outline-primary");
    e_8.setAttribute("for", "judgebtnradio"+(formlabel-1)*2+1);
    e_8.appendChild(document.createTextNode("正确"));
    e_6.appendChild(e_8);
    var e_9 = document.createElement("input");
    e_9.setAttribute("type", "radio");
    e_9.setAttribute("class", "btn-check");
    e_9.setAttribute("name", "judgebtnradio"+formlabel);
    e_9.setAttribute("id", "judgebtnradio"+(formlabel-1)*2+2);
    e_9.setAttribute("autocomplete", "off");
    if(checedB==1){
        e_9.setAttribute("checked", "true");
    }
    e_6.appendChild(e_9);
    var e_10 = document.createElement("label");
    e_10.setAttribute("class", "btn btn-outline-danger");
    e_10.setAttribute("for", "judgebtnradio"+(formlabel-1)*2+2);
    e_10.appendChild(document.createTextNode("错误"));
    e_6.appendChild(e_10);
    e_5.appendChild(e_6);
    e_0.appendChild(e_5);
    return e_0;
}


function createmultipleNode(formlabel) {
    var e_0 = document.createElement("div");
    e_0.setAttribute("class", "multiple_question-group animate__animated animate__fadeIn hvr-grow-shadow");
    var e_1 = document.createElement("div");
    e_1.setAttribute("class", "display-flex");
    var e_2 = document.createElement("label");
    e_2.setAttribute("class", "form-label");
    e_2.appendChild(document.createTextNode(formlabel));
    e_1.appendChild(e_2);


    var e_mark = document.createElement("input");
    e_mark.setAttribute("id", "multiplemark"+formlabel);
    e_mark.setAttribute("class", "mark");
    e_mark.setAttribute("type", "number");
    e_mark.setAttribute("min", "0");
    e_mark.setAttribute("max", "100"+formlabel);
    e_mark.setAttribute("value", "1");
    e_1.appendChild(e_mark);

    
    var e_3 = document.createElement("button");
    e_3.setAttribute("type", "button");
    e_3.setAttribute("style", "float: right;");
    e_3.setAttribute("class", "removeclass btn btn-danger");
    e_3.appendChild(document.createTextNode("删除"));
    e_1.appendChild(e_3);
    e_0.appendChild(e_1);
    var e_4 = document.createElement("input");
    e_4.setAttribute("type", "text");
    e_4.setAttribute("name", "ques_title");
    e_4.setAttribute("class", "form-control");
    e_4.setAttribute("placeholder", "题目内容");
    e_4.setAttribute("autocomplete", "off");
    e_0.appendChild(e_4);
    var e_5 = document.createElement("div");
    e_5.setAttribute("class", "input-group mb-3");
    var e_6 = document.createElement("div");
    e_6.setAttribute("class", "btn-group");
    e_6.setAttribute("style", "width:100%");
    e_6.setAttribute("role", "group");
    e_6.setAttribute("aria-label", "Basic radio toggle button group");
    var e_7 = document.createElement("input");
    e_7.setAttribute("type", "checkbox");
    e_7.setAttribute("class", "btn-check");
    e_7.setAttribute("name", "mutiplebtnradio"+formlabel);
    e_7.setAttribute("id", "mutiplebtnradio"+(formlabel-1)*4+1);
    e_7.setAttribute("autocomplete", "off");
    e_6.appendChild(e_7);
    var e_8 = document.createElement("label");
    e_8.setAttribute("class", "btn btn-outline-primary");
    e_8.setAttribute("for", "mutiplebtnradio"+(formlabel-1)*4+1);
    e_8.appendChild(document.createTextNode("A"));
    e_6.appendChild(e_8);
    var e_9 = document.createElement("input");
    e_9.setAttribute("type", "text");
    e_9.setAttribute("class", "form-control");
    e_9.setAttribute("name", "ques_option");
    e_9.setAttribute("placeholder", "选项A");
    e_9.setAttribute("aria-label", "Server");
    e_6.appendChild(e_9);
    var e_10 = document.createElement("input");
    e_10.setAttribute("type", "checkbox");
    e_10.setAttribute("class", "btn-check");
    e_10.setAttribute("name", "mutiplebtnradio"+formlabel);
    e_10.setAttribute("id", "mutiplebtnradio"+(formlabel-1)*4+2);
    e_10.setAttribute("autocomplete", "off");
    e_6.appendChild(e_10);
    var e_11 = document.createElement("label");
    e_11.setAttribute("class", "btn btn-outline-primary");
    e_11.setAttribute("for", "mutiplebtnradio"+(formlabel-1)*4+2);
    e_11.appendChild(document.createTextNode("B"));
    e_6.appendChild(e_11);
    var e_12 = document.createElement("input");
    e_12.setAttribute("type", "text");
    e_12.setAttribute("class", "form-control");
    e_12.setAttribute("name", "ques_option");
    e_12.setAttribute("placeholder", "选项B");
    e_12.setAttribute("aria-label", "Server");
    e_6.appendChild(e_12);
    var e_13 = document.createElement("input");
    e_13.setAttribute("type", "checkbox");
    e_13.setAttribute("class", "btn-check");
    e_13.setAttribute("name", "mutiplebtnradio"+formlabel);
    e_13.setAttribute("id", "mutiplebtnradio"+(formlabel-1)*4+3);
    e_13.setAttribute("autocomplete", "off");
    e_6.appendChild(e_13);
    var e_14 = document.createElement("label");
    e_14.setAttribute("class", "btn btn-outline-primary");
    e_14.setAttribute("for", "mutiplebtnradio"+(formlabel-1)*4+3);
    e_14.appendChild(document.createTextNode("C"));
    e_6.appendChild(e_14);
    var e_15 = document.createElement("input");
    e_15.setAttribute("type", "text");
    e_15.setAttribute("class", "form-control");
    e_15.setAttribute("name", "ques_option");
    e_15.setAttribute("placeholder", "选项C");
    e_15.setAttribute("aria-label", "Server");
    e_6.appendChild(e_15);
    var e_16 = document.createElement("input");
    e_16.setAttribute("type", "checkbox");
    e_16.setAttribute("class", "btn-check");
    e_16.setAttribute("name", "mutiplebtnradio"+formlabel);
    e_16.setAttribute("id", "mutiplebtnradio"+(formlabel-1)*4+4);
    e_16.setAttribute("autocomplete", "off");
    e_6.appendChild(e_16);
    var e_17 = document.createElement("label");
    e_17.setAttribute("class", "btn btn-outline-primary");
    e_17.setAttribute("for", "mutiplebtnradio"+(formlabel-1)*4+4);
    e_17.appendChild(document.createTextNode("D"));
    e_6.appendChild(e_17);
    var e_18 = document.createElement("input");
    e_18.setAttribute("type", "text");
    e_18.setAttribute("class", "form-control");
    e_18.setAttribute("name", "ques_option");
    e_18.setAttribute("placeholder", "选项D");
    e_18.setAttribute("aria-label", "Server");
    e_6.appendChild(e_18);
    e_5.appendChild(e_6);
    e_0.appendChild(e_5);
    return e_0;
}


function editmultipleNode(formlabel,title,checedA,optionA,checedB,optionB,checedC,optionC,checedD,optionD,mark) {
    var e_0 = document.createElement("div");
    e_0.setAttribute("class", "multiple_question-group animate__animated animate__fadeIn hvr-grow-shadow");
    var e_1 = document.createElement("div");
    e_1.setAttribute("class", "display-flex");
    var e_2 = document.createElement("label");
    e_2.setAttribute("class", "form-label");
    e_2.appendChild(document.createTextNode(formlabel));
    e_1.appendChild(e_2);

    var e_mark = document.createElement("input");
    e_mark.setAttribute("id", "multiplemark"+formlabel);
    e_mark.setAttribute("class", "mark");
    e_mark.setAttribute("type", "number");
    e_mark.setAttribute("min", "0");
    e_mark.setAttribute("max", "100"+formlabel);
    e_mark.setAttribute("value", mark);
    e_1.appendChild(e_mark);

    var e_3 = document.createElement("button");
    e_3.setAttribute("type", "button");
    e_3.setAttribute("style", "float: right;");
    e_3.setAttribute("class", "removeclass btn btn-danger");
    e_3.appendChild(document.createTextNode("删除"));
    e_1.appendChild(e_3);
    e_0.appendChild(e_1);
    var e_4 = document.createElement("input");
    e_4.setAttribute("type", "text");
    e_4.setAttribute("name", "ques_title");
    e_4.setAttribute("class", "form-control");
    e_4.setAttribute("placeholder", "题目内容");
    e_4.setAttribute("autocomplete", "off");
    e_4.value = title
    e_0.appendChild(e_4);
    var e_5 = document.createElement("div");
    e_5.setAttribute("class", "input-group mb-3");
    var e_6 = document.createElement("div");
    e_6.setAttribute("class", "btn-group");
    e_6.setAttribute("style", "width:100%");
    e_6.setAttribute("role", "group");
    e_6.setAttribute("aria-label", "Basic radio toggle button group");
    var e_7 = document.createElement("input");
    e_7.setAttribute("type", "checkbox");
    e_7.setAttribute("class", "btn-check");
    e_7.setAttribute("name", "mutiplebtnradio"+formlabel);
    e_7.setAttribute("id", "mutiplebtnradio"+(formlabel-1)*4+1);
    e_7.setAttribute("autocomplete", "off");
    if(checedA==1){
        e_7.setAttribute("checked", "true");
    }
    e_6.appendChild(e_7);
    var e_8 = document.createElement("label");
    e_8.setAttribute("class", "btn btn-outline-primary");
    e_8.setAttribute("for", "mutiplebtnradio"+(formlabel-1)*4+1);
    e_8.appendChild(document.createTextNode("A"));
    e_6.appendChild(e_8);
    var e_9 = document.createElement("input");
    e_9.setAttribute("type", "text");
    e_9.setAttribute("class", "form-control");
    e_9.setAttribute("name", "ques_option");
    e_9.setAttribute("placeholder", "选项A");
    e_9.setAttribute("aria-label", "Server");
    e_9.value = optionA
    e_6.appendChild(e_9);
    var e_10 = document.createElement("input");
    e_10.setAttribute("type", "checkbox");
    e_10.setAttribute("class", "btn-check");
    e_10.setAttribute("name", "mutiplebtnradio"+formlabel);
    e_10.setAttribute("id", "mutiplebtnradio"+(formlabel-1)*4+2);
    e_10.setAttribute("autocomplete", "off");
    if(checedB==1){
        e_10.setAttribute("checked", "true");
    }
    e_6.appendChild(e_10);
    var e_11 = document.createElement("label");
    e_11.setAttribute("class", "btn btn-outline-primary");
    e_11.setAttribute("for", "mutiplebtnradio"+(formlabel-1)*4+2);
    e_11.appendChild(document.createTextNode("B"));
    e_6.appendChild(e_11);
    var e_12 = document.createElement("input");
    e_12.setAttribute("type", "text");
    e_12.setAttribute("class", "form-control");
    e_12.setAttribute("name", "ques_option");
    e_12.setAttribute("placeholder", "选项B");
    e_12.setAttribute("aria-label", "Server");
    e_12.value = optionB
    e_6.appendChild(e_12);
    var e_13 = document.createElement("input");
    e_13.setAttribute("type", "checkbox");
    e_13.setAttribute("class", "btn-check");
    e_13.setAttribute("name", "mutiplebtnradio"+formlabel);
    e_13.setAttribute("id", "mutiplebtnradio"+(formlabel-1)*4+3);
    e_13.setAttribute("autocomplete", "off");
    if(checedC==1){
        e_13.setAttribute("checked", "true");
    }
    e_6.appendChild(e_13);
    var e_14 = document.createElement("label");
    e_14.setAttribute("class", "btn btn-outline-primary");
    e_14.setAttribute("for", "mutiplebtnradio"+(formlabel-1)*4+3);
    e_14.appendChild(document.createTextNode("C"));
    e_6.appendChild(e_14);
    var e_15 = document.createElement("input");
    e_15.setAttribute("type", "text");
    e_15.setAttribute("class", "form-control");
    e_15.setAttribute("name", "ques_option");
    e_15.setAttribute("placeholder", "选项C");
    e_15.setAttribute("aria-label", "Server");
    e_15.value = optionC
    e_6.appendChild(e_15);
    var e_16 = document.createElement("input");
    e_16.setAttribute("type", "checkbox");
    e_16.setAttribute("class", "btn-check");
    e_16.setAttribute("name", "mutiplebtnradio"+formlabel);
    e_16.setAttribute("id", "mutiplebtnradio"+(formlabel-1)*4+4);
    e_16.setAttribute("autocomplete", "off");
    if(checedD==1){
        e_16.setAttribute("checked", "true");
    }
    e_6.appendChild(e_16);
    var e_17 = document.createElement("label");
    e_17.setAttribute("class", "btn btn-outline-primary");
    e_17.setAttribute("for", "mutiplebtnradio"+(formlabel-1)*4+4);
    e_17.appendChild(document.createTextNode("D"));
    e_6.appendChild(e_17);
    var e_18 = document.createElement("input");
    e_18.setAttribute("type", "text");
    e_18.setAttribute("class", "form-control");
    e_18.setAttribute("name", "ques_option");
    e_18.setAttribute("placeholder", "选项D");
    e_18.setAttribute("aria-label", "Server");
    e_18.value = optionD
    e_6.appendChild(e_18);
    e_5.appendChild(e_6);
    e_0.appendChild(e_5);
    return e_0;
}


function createanswerNode(all_index,index,title,optionA,optionB,optionC,optionD) {
    var e_0 = document.createElement("div");
    e_0.setAttribute("class", "question-group");
    e_0.setAttribute("hidden",true);
    e_0.setAttribute("id","qg"+all_index);
    var e_1 = document.createElement("label");
    e_1.setAttribute("class", "form-label");
    e_1.innerText='单选题'
    var e_1_1 = document.createElement("label");
    e_1_1.setAttribute("class", "single_count-label");
    e_1_1.setAttribute("style", "float: right;");
    var e_1_2 = document.createElement("label");
    e_1_2.setAttribute("class", "index-label");
    e_1_2.setAttribute("style", "float: right;");
    e_1_2.innerText=index+1
    e_0.appendChild(e_1);
    e_0.appendChild(e_1_1);
    e_0.appendChild(e_1_2);
    var e_2 = document.createElement("input");
    e_2.setAttribute("type", "text");
    e_2.setAttribute("name", "ques_title");
    e_2.setAttribute("class", "form-control");
    e_2.setAttribute("placeholder", "题目内容");
    e_2.setAttribute("autocomplete", "off");
    e_2.value = title
    e_0.appendChild(e_2);
    var e_3 = document.createElement("div");
    e_3.setAttribute("class", "btn-group-vertical my_btn_vertical");
    e_3.setAttribute("role", "group");
    e_3.setAttribute("aria-label", "Basic radio toggle button group");
    var e_4 = document.createElement("div");
    e_4.setAttribute("class", "container question-option");
    var e_5 = document.createElement("input");
    e_5.setAttribute("type", "radio");
    e_5.setAttribute("class", "btn-check my_radio");
    e_5.setAttribute("name", "btn_radio"+index);
    e_5.setAttribute("id", "btnradio"+((index)*4));
    e_5.setAttribute("placeholder", "选项A");
    e_5.setAttribute("aria-label", "Server");
    e_4.appendChild(e_5);
    var e_6 = document.createElement("label");
    e_6.setAttribute("class", "btn btn-outline-primary mybtn-label");
    e_6.setAttribute("for", "btnradio"+((index)*4));
    e_6.setAttribute("id", "btntext"+((index)*4));
    //console.log(e_6)
    e_6.innerText='A: '+optionA
    e_4.appendChild(e_6);
    e_3.appendChild(e_4);
    var e_7 = document.createElement("div");
    e_7.setAttribute("class", "container question-option");
    var e_8 = document.createElement("input");
    e_8.setAttribute("type", "radio");
    e_8.setAttribute("class", "btn-check my_radio");
    e_8.setAttribute("name", "btn_radio"+index);
    e_8.setAttribute("id", "btnradio"+((index)*4+1));
    
    e_8.setAttribute("placeholder", "选项B");
    e_8.setAttribute("aria-label", "Server");
    e_7.appendChild(e_8);
    var e_9 = document.createElement("label");
    e_9.setAttribute("class", "btn btn-outline-primary mybtn-label");
    e_9.setAttribute("for", "btnradio"+((index)*4+1));
    e_9.setAttribute("id", "btntext"+((index)*4+1));
    e_9.innerText ='B: '+optionB
    e_7.appendChild(e_9);
    e_3.appendChild(e_7);
    var e_10 = document.createElement("div");
    e_10.setAttribute("class", "container question-option");
    var e_11 = document.createElement("input");
    e_11.setAttribute("type", "radio");
    e_11.setAttribute("class", "btn-check my_radio");
    e_11.setAttribute("name", "btn_radio"+index);
    e_11.setAttribute("id", "btnradio"+((index)*4+2));
    e_11.setAttribute("placeholder", "选项C");
    e_11.setAttribute("aria-label", "Server");
    e_10.appendChild(e_11);
    var e_12 = document.createElement("label");
    e_12.setAttribute("class", "btn btn-outline-primary mybtn-label");
    e_12.setAttribute("for", "btnradio"+((index)*4+2));
    e_12.setAttribute("id", "btntext"+((index)*4+2));
    e_12.innerText = 'C: '+optionC
    e_10.appendChild(e_12);
    e_3.appendChild(e_10);
    var e_13 = document.createElement("div");
    e_13.setAttribute("class", "container question-option");
    var e_14 = document.createElement("input");
    e_14.setAttribute("type", "radio");
    e_14.setAttribute("class", "btn-check my_radio");
    e_14.setAttribute("name", "btn_radio"+index);
    e_14.setAttribute("id", "btnradio"+((index)*4+3));
    e_14.setAttribute("placeholder", "选项D");
    e_14.setAttribute("aria-label", "Server");
    e_13.appendChild(e_14);
    var e_15 = document.createElement("label");
    e_15.setAttribute("class", "btn btn-outline-primary mybtn-label");
    e_15.setAttribute("for", "btnradio"+((index)*4+3));
    e_15.setAttribute("id", "btntext"+((index)*4+3));
    e_15.innerText = 'D: '+optionD
    e_13.appendChild(e_15);
    e_3.appendChild(e_13);
    e_0.appendChild(e_3);
    return e_0;
}


function createanswerjudgeNode(all_index,index,title) {
    var e_0 = document.createElement("div");
    e_0.setAttribute("class", "judgequestion-group");
    e_0.setAttribute("hidden",true);
    e_0.setAttribute("id", "qg"+all_index);
    var e_1 = document.createElement("label");
    e_1.setAttribute("class", "form-label");
    e_1.appendChild(document.createTextNode("判断题"));
    e_0.appendChild(e_1);
    var e_2 = document.createElement("label");
    e_2.setAttribute("class", "judge_count-label");
    e_2.setAttribute("style", "float: right;");
    e_0.appendChild(e_2);
    var e_3 = document.createElement("label");
    e_3.setAttribute("class", "index-label");
    e_3.setAttribute("style", "float: right;");
    e_3.appendChild(document.createTextNode(index+1));
    e_0.appendChild(e_3);
    var e_4 = document.createElement("input");
    e_4.setAttribute("type", "text");
    e_4.setAttribute("name", "ques_title");
    e_4.setAttribute("class", "form-control");
    e_4.setAttribute("placeholder", "题目内容");
    e_4.setAttribute("autocomplete", "off");
    e_4.value = title
    e_0.appendChild(e_4);
    var e_5 = document.createElement("div");
    e_5.setAttribute("class", "btn-group-vertical my_btn_vertical");
    e_5.setAttribute("role", "group");
    e_5.setAttribute("aria-label", "Basic radio toggle button group");
    var e_6 = document.createElement("div");
    e_6.setAttribute("class", "container question-option");
    var e_7 = document.createElement("input");
    e_7.setAttribute("type", "radio");
    e_7.setAttribute("class", "btn-check my_radio");
    e_7.setAttribute("name", "btnjudgeradio"+index);
    e_7.setAttribute("id", "btnjudgeradio"+((index)*2));
    e_7.setAttribute("aria-label", "Server");
    e_6.appendChild(e_7);
    var e_8 = document.createElement("label");
    e_8.setAttribute("class", "btn btn-outline-primary mybtn-label");
    e_8.setAttribute("for", "btnjudgeradio"+((index)*2));
    e_8.setAttribute("id", "judgebtntext"+((index)*2));
    e_8.appendChild(document.createTextNode("正确"));
    e_6.appendChild(e_8);
    e_5.appendChild(e_6);
    var e_9 = document.createElement("div");
    e_9.setAttribute("class", "container question-option");
    var e_10 = document.createElement("input");
    e_10.setAttribute("type", "radio");
    e_10.setAttribute("class", "btn-check my_radio");
    e_10.setAttribute("name", "btnjudgeradio"+index);
    e_10.setAttribute("id", "btnjudgeradio"+((index)*2+1));
    e_10.setAttribute("aria-label", "Server");
    e_9.appendChild(e_10);
    var e_11 = document.createElement("label");
    e_11.setAttribute("class", "btn btn-outline-primary mybtn-label");
    e_11.setAttribute("for", "btnjudgeradio"+((index)*2+1));
    e_11.setAttribute("id", "judgebtntext"+((index)*2+1));
    e_11.appendChild(document.createTextNode("错误 "));
    e_9.appendChild(e_11);
    e_5.appendChild(e_9);
    e_0.appendChild(e_5);
    return e_0;
}


function createanswermultipleNode(all_index,index,title,optionA,optionB,optionC,optionD) {
    var e_0 = document.createElement("div");
    e_0.setAttribute("class", "multiplequestion-group");
    e_0.setAttribute("hidden",true);
    e_0.setAttribute("id","qg"+all_index);
    var e_1 = document.createElement("label");
    e_1.setAttribute("class", "form-label");
    e_1.innerText='多选题'
    var e_1_1 = document.createElement("label");
    e_1_1.setAttribute("class", "multiple_count-label");
    e_1_1.setAttribute("style", "float: right;");
    var e_1_2 = document.createElement("label");
    e_1_2.setAttribute("class", "index-label");
    e_1_2.setAttribute("style", "float: right;");
    e_1_2.innerText=index+1
    e_0.appendChild(e_1);
    e_0.appendChild(e_1_1);
    e_0.appendChild(e_1_2);
    var e_2 = document.createElement("input");
    e_2.setAttribute("type", "text");
    e_2.setAttribute("name", "ques_title");
    e_2.setAttribute("class", "form-control");
    e_2.setAttribute("placeholder", "题目内容");
    e_2.setAttribute("autocomplete", "off");
    e_2.value = title
    e_0.appendChild(e_2);
    var e_3 = document.createElement("div");
    e_3.setAttribute("class", "btn-group-vertical my_btn_vertical");
    e_3.setAttribute("role", "group");
    e_3.setAttribute("aria-label", "Basic radio toggle button group");
    var e_4 = document.createElement("div");
    e_4.setAttribute("class", "container question-option");
    var e_5 = document.createElement("input");
    e_5.setAttribute("type", "checkbox");
    e_5.setAttribute("class", "btn-check my_radio");
    e_5.setAttribute("name", "btnmultipleradio"+index);
    e_5.setAttribute("id", "btnmultipleradio"+((index)*4));
    e_5.setAttribute("placeholder", "选项A");
    e_5.setAttribute("aria-label", "Server");
    e_4.appendChild(e_5);
    var e_6 = document.createElement("label");
    e_6.setAttribute("class", "btn btn-outline-primary mybtn-label");
    e_6.setAttribute("for", "btnmultipleradio"+((index)*4));
    e_6.setAttribute("id", "multiplebtntext"+((index)*4));
    //console.log(e_6)
    e_6.innerText='A: '+optionA
    e_4.appendChild(e_6);
    e_3.appendChild(e_4);
    var e_7 = document.createElement("div");
    e_7.setAttribute("class", "container question-option");
    var e_8 = document.createElement("input");
    e_8.setAttribute("type", "checkbox");
    e_8.setAttribute("class", "btn-check my_radio");
    e_8.setAttribute("name", "btnmultipleradio"+index);
    e_8.setAttribute("id", "btnmultipleradio"+((index)*4+1));
    
    e_8.setAttribute("placeholder", "选项B");
    e_8.setAttribute("aria-label", "Server");
    e_7.appendChild(e_8);
    var e_9 = document.createElement("label");
    e_9.setAttribute("class", "btn btn-outline-primary mybtn-label");
    e_9.setAttribute("for", "btnmultipleradio"+((index)*4+1));
    e_9.setAttribute("id", "multiplebtntext"+((index)*4+1));
    e_9.innerText ='B: '+optionB
    e_7.appendChild(e_9);
    e_3.appendChild(e_7);
    var e_10 = document.createElement("div");
    e_10.setAttribute("class", "container question-option");
    var e_11 = document.createElement("input");
    e_11.setAttribute("type", "checkbox");
    e_11.setAttribute("class", "btn-check my_radio");
    e_11.setAttribute("name", "btnmultipleradio"+index);
    e_11.setAttribute("id", "btnmultipleradio"+((index)*4+2));
    e_11.setAttribute("placeholder", "选项C");
    e_11.setAttribute("aria-label", "Server");
    e_10.appendChild(e_11);
    var e_12 = document.createElement("label");
    e_12.setAttribute("class", "btn btn-outline-primary mybtn-label");
    e_12.setAttribute("for", "btnmultipleradio"+((index)*4+2));
    e_12.setAttribute("id", "multiplebtntext"+((index)*4+2));
    e_12.innerText = 'C: '+optionC
    e_10.appendChild(e_12);
    e_3.appendChild(e_10);
    var e_13 = document.createElement("div");
    e_13.setAttribute("class", "container question-option");
    var e_14 = document.createElement("input");
    e_14.setAttribute("type", "checkbox");
    e_14.setAttribute("class", "btn-check my_radio");
    e_14.setAttribute("name", "btnmultipleradio"+index);
    e_14.setAttribute("id", "btnmultipleradio"+((index)*4+3));
    e_14.setAttribute("placeholder", "选项D");
    e_14.setAttribute("aria-label", "Server");
    e_13.appendChild(e_14);
    var e_15 = document.createElement("label");
    e_15.setAttribute("class", "btn btn-outline-primary mybtn-label");
    e_15.setAttribute("for", "btnmultipleradio"+((index)*4+3));
    e_15.setAttribute("id", "multiplebtntext"+((index)*4+3));
    e_15.innerText = 'D: '+optionD
    e_13.appendChild(e_15);
    e_3.appendChild(e_13);
    e_0.appendChild(e_3);
    return e_0;
}

/*function createNode(type,index,count,title,optionA,optionB,optionC,optionD) {
    var e_0 = document.createElement("div");
    e_0.setAttribute("class", "question-group");
    e_0.setAttribute("hidden",true);
    e_0.setAttribute("id","qg"+index);
    var e_1 = document.createElement("label");
    e_1.setAttribute("class", "form-label");
    e_1.innerText=type
    var e_1_1 = document.createElement("label");
    e_1_1.setAttribute("class", "count-label");
    e_1_1.setAttribute("style", "float: right;");
    e_1_1.innerText='/'+count
    var e_1_2 = document.createElement("label");
    e_1_2.setAttribute("class", "index-label");
    e_1_2.setAttribute("style", "float: right;");
    e_1_2.innerText=index+1
    e_0.appendChild(e_1);
    e_0.appendChild(e_1_1);
    e_0.appendChild(e_1_2);
    var e_2 = document.createElement("input");
    e_2.setAttribute("type", "text");
    e_2.setAttribute("name", "ques_title");
    e_2.setAttribute("class", "form-control");
    e_2.setAttribute("placeholder", "题目内容");
    e_2.setAttribute("autocomplete", "off");
    e_2.value = title
    e_0.appendChild(e_2);
    var e_3 = document.createElement("div");
    e_3.setAttribute("class", "btn-group-vertical my_btn_vertical");
    e_3.setAttribute("role", "group");
    e_3.setAttribute("aria-label", "Basic radio toggle button group");
    var e_4 = document.createElement("div");
    e_4.setAttribute("class", "container question-option");
    var e_5 = document.createElement("input");
    e_5.setAttribute("type", "radio");
    e_5.setAttribute("class", "btn-check my_radio");
    e_5.setAttribute("name", "btn_radio"+index);
    e_5.setAttribute("id", "btnradio"+((index)*4));
    e_5.setAttribute("placeholder", "选项A");
    e_5.setAttribute("aria-label", "Server");
    e_4.appendChild(e_5);
    var e_6 = document.createElement("label");
    e_6.setAttribute("class", "btn btn-outline-primary mybtn-label");
    e_6.setAttribute("for", "btnradio"+((index)*4));
    e_6.setAttribute("id", "btntext"+((index)*4));
    //console.log(e_6)
    e_6.innerText='A: '+optionA
    e_4.appendChild(e_6);
    e_3.appendChild(e_4);
    var e_7 = document.createElement("div");
    e_7.setAttribute("class", "container question-option");
    var e_8 = document.createElement("input");
    e_8.setAttribute("type", "radio");
    e_8.setAttribute("class", "btn-check my_radio");
    e_8.setAttribute("name", "btn_radio"+index);
    e_8.setAttribute("id", "btnradio"+((index)*4+1));
    
    e_8.setAttribute("placeholder", "选项B");
    e_8.setAttribute("aria-label", "Server");
    e_7.appendChild(e_8);
    var e_9 = document.createElement("label");
    e_9.setAttribute("class", "btn btn-outline-primary mybtn-label");
    e_9.setAttribute("for", "btnradio"+((index)*4+1));
    e_9.setAttribute("id", "btntext"+((index)*4+1));
    e_9.innerText ='B: '+optionB
    e_7.appendChild(e_9);
    e_3.appendChild(e_7);
    var e_10 = document.createElement("div");
    e_10.setAttribute("class", "container question-option");
    var e_11 = document.createElement("input");
    e_11.setAttribute("type", "radio");
    e_11.setAttribute("class", "btn-check my_radio");
    e_11.setAttribute("name", "btn_radio"+index);
    e_11.setAttribute("id", "btnradio"+((index)*4+2));
    e_11.setAttribute("placeholder", "选项C");
    e_11.setAttribute("aria-label", "Server");
    e_10.appendChild(e_11);
    var e_12 = document.createElement("label");
    e_12.setAttribute("class", "btn btn-outline-primary mybtn-label");
    e_12.setAttribute("for", "btnradio"+((index)*4+2));
    e_12.setAttribute("id", "btntext"+((index)*4+2));
    e_12.innerText = 'C: '+optionC
    e_10.appendChild(e_12);
    e_3.appendChild(e_10);
    var e_13 = document.createElement("div");
    e_13.setAttribute("class", "container question-option");
    var e_14 = document.createElement("input");
    e_14.setAttribute("type", "radio");
    e_14.setAttribute("class", "btn-check my_radio");
    e_14.setAttribute("name", "btn_radio"+index);
    e_14.setAttribute("id", "btnradio"+((index)*4+3));
    e_14.setAttribute("placeholder", "选项D");
    e_14.setAttribute("aria-label", "Server");
    e_13.appendChild(e_14);
    var e_15 = document.createElement("label");
    e_15.setAttribute("class", "btn btn-outline-primary mybtn-label");
    e_15.setAttribute("for", "btnradio"+((index)*4+3));
    e_15.setAttribute("id", "btntext"+((index)*4+3));
    e_15.innerText = 'D: '+optionD
    e_13.appendChild(e_15);
    e_3.appendChild(e_13);
    e_0.appendChild(e_3);
    return e_0;
}*/