console.log("조윤지주문");

  function make_order(){
    //주문 완료 결과 확인

    let data = {

        "order-name":$("#order-name").val(),
        "order-address":$("#order-address").val(),
        "order-phone":$("#order-phone").val()
        }

    console.log(data);

    $.ajax({
      type: "POST", // POST 방식으로 요청하겠다.
      url: "/order_list", // /order_list라는 url에 요청하겠다.
      data: {
        name_give: data["order-name"],
        address_give: data["order-address"]
        phone_give: data["order-phone"]
        }, // 데이터를 주는 방법
      success: function(result){ // 성공하면
        console.log(result); // 콘솔 창에 결과를 찍어주자
        if(result["result"]=='success'){
                alert("주문이 완료되었습니다.")
                 window.location.reload(true);
        }else{
                alert("주문되지 않았습니다. 관리자에게 문의하세요. 1588-1588")

        }
      }
    })