$(document).ready(function() {

var MaxInputs       = 8; //maximum input boxes allowed
var InputsWrapper   = $("#InputsWrapper"); //Input boxes wrapper ID
var AddButton       = $("#AddMoreFileBox"); //Add button ID

var x = InputsWrapper.length; //initial text box count
var FieldCount=1; //to keep track of text box added

$(AddButton).click(function (e)  //on add input button click
{
    if(x <= MaxInputs) //max input box allowed
    {
        FieldCount++; //text box added increment
        //add input box
        $(InputsWrapper).append('<div class="row mb-4"><p class="left-division"><input type="text" placeholder="Enter ingredient" class="form-control ingredient_list" name="ingredient[]" id="field_'+ FieldCount +'" value=""/></p><p class="right-division"><input type="text" placeholder="Amount (g)" class="form-control ingredient_list" name="ingredient[]" id="field_'+ FieldCount +'" value=""/></p><a href="#" class="btn btn-danger removeclass">×</a></div>');
        x++; //text box increment
    }
    return false;
});

$("body").on("click",".removeclass", function(e){ //user click on remove text
    if( x > 1 ) {
        $(this).parent('div').remove(); //remove text box
         x--; //decrement textbox
    }
    return false;
})

});
