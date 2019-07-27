console.log("조윤지주문");

  function make_order(){
    //주문 완료 결과 확인

    let name = $("#name").val();
    let address = $("#address").val();
    let phone = $("#number").val();


    $.ajax({
      type: "POST", // POST 방식으로 요청하겠다.
      data: {
        name_give: name,
        address_give: address,
        phone_give: number
        }, // 데이터를 주는 방법
      success: function(response){ // 성공하면
            console.log(response);
        if(response['result']=='success'){
                alert("주문이 완료되었습니다.")
                 window.location.reload(true);
        }else{
                alert("주문되지 않았습니다. 관리자에게 문의하세요. 1588-1588")

        }

      }
    })
  }