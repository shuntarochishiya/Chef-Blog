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
        $(InputsWrapper).append("<div>"+
                        '<div style="float:left; width:69%;">'+
                            '<select class="form-control form-control-lg" id="cuisine" name="ingredient"><option value="1">Mushroom</option><option value="3">Carrot</option><option value="4">Radish</option><option value="8">Cabbage</option><option value="9">Pinecone</option><option value="11">Jeuyun chili</option><option value="17">Raw meat</option><option value="18">Bird egg</option><option value="19">Matsutake</option><option value="20">Fowl</option><option value="2">Sweet flower</option><option value="5">Snapdragon</option><option value="6">Mint</option><option value="10">Lotus head</option><option value="12">Qingxin</option><option value="13">Violetgrass</option><option value="15">Small lamp grass</option><option value="16">Calla lily</option><option value="21">Crab</option><option value="22">Crab roe</option><option value="23">Salt</option><option value="24">Onion</option><option value="25">Milk</option><option value="26">Tomato</option><option value="27">Potato</option><option value="28">Fish</option><option value="30">Almond</option><option value="7">Wheat</option><option value="31">Bamboo shoot</option><option value="32">Rice</option><option value="33">Shrimp meat</option><option value="34">Chilled meat</option><option value="35">Eel meat</option><option value="36">Glabrous beans</option><option value="37">Mysterious meat</option><option value="38">Coffee beans</option><option value="39">Fermented juice</option><option value="40">Sakura blossom</option><option value="41">Seagrass</option><option value="42">Lavender melon</option><option value="43">Harra fruit</option><option value="44">Zaytun peach</option><option value="45">Sumeru rose</option><option value="46">Ajilenakh nut</option><option value="47">Marcotte</option><option value="48">Tidalga</option><option value="49">Flour</option><option value="50">Cream</option><option value="51">Smoked fowl</option><option value="52">Butter</option><option value="53">Ham</option><option value="54">Sugar</option><option value="55">Jam</option><option value="56">Cheese</option><option value="57">Bacon</option><option value="58">Sausage</option><option value="59">Spice</option><option value="60">Strange meat product</option><option value="14">Berry</option><option value="29">Tofu</option><option value="0">Padisarah</option></select>'+
                        '</div><div style="float:right; width:29%;">'+
                            '<input class="form-control form-control-lg" id="amount" name="amount" placeholder="Amount" required="" type="text" value="">'+
                        '</div>'+
                        '<a href="#" class="btn btn-danger removeclass">×</a></div>');
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
