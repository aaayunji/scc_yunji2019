console.log("조윤지");

window.onload =function(){
    get_posting();
}

function get_posting(){
  $.ajax({
    type: "GET",
    url: "/post",
    data: {},
    success: function(response){
      console.log(response);
      // back end 값이 response에 담겨서 나온다
      for(let i = 0; i<response["articles"].length;i++){

            console.log(response["articles"][i]['url'],response["articles"][i]['comment'])
            append_card(response["articles"][i]['url'],response["articles"][i]['comment']);

//            console.log(response["articles"].length)
//            let count = response["articles"].length;
            }
           }
         })
      }

// $(document).ready life cycle 더 빠른 함수

        function append_card(url,comment){

        console.log(url,comment)
        let temp_html = '<div class="card">\
        <img class="card-img-top" src="https://www.fodors.com/wp-content/uploads/2018/10/4_UltimateRome_PiazzaNavona-975x650.jpg" alt="Card image cap">\
        <div class="card-body">\
          <a class="card-title" target="_blank" href="'+url+'">예를 들면 이렇게 카드가 나옵니다!!</a>\
          <p class="card-text">여기에 기사 내용이 들어가겠죠</p>\
          <p class="card-text comment">'+comment+'</p>\
        </div>\
      </div>\
    </div>';

      console.log(temp_html);
      $('#cards-box').append(temp_html);
        }

/**

이벤트 순서를 강제, 가장 먼저 실행 시키고 싶을때 사용하는 함수

**/

  //값가져오기
  //$("#posting-url").val();
  //$("#posting-url").val('조윤지');

  //$("#posting-box").hide();
  // $("#posting-box").css("display","none");

  //$("#posting-box").show();
  //$("#posting-box").css("display","block");



  //let temp_html =+ '<div class="card">'
  //    temp_html =+ '<img class="card-img-top" src="https://www.fodors.com/wp-content/uploads/2018/10/4_UltimateRome_PiazzaNavona-975x650.jpg" alt="Card image cap">'
  //    temp_html =+ '<div class="card-body">'
  //    temp_html =+ '<h5 class="card-title">예를 들면 이렇게 카드가 나옵니다!!</h5>'
  //    temp_html =+ '<p class="card-text">여기에 기사 내용이 들어가겠죠</p>'
  //    temp_html =+ '<p class="card-text comment">여기엔 코멘트가 들어갑니다</p>'
  //    temp_html =+ '</div>'
  //    temp_html =+ '</div>'

//  let temp_html = '<div class="card">\
//        <img class="card-img-top" src="https://www.fodors.com/wp-content/uploads/2018/10/4_UltimateRome_PiazzaNavona-975x650.jpg" alt="Card image cap">\
//        <div class="card-body">\
//          <h5 class="card-title">예를 들면 이렇게 카드가 나옵니다!!</h5>\
//          <p class="card-text">여기에 기사 내용이 들어가겠죠</p>\
//          <p class="card-text comment">여기엔 코멘트가 들어갑니다</p>\
//        </div>\
//      </div>\
//    </div>';


//  console.log(temp_html);

  function openclose(){
  		// id 값 posting-box의 display 값이 block 이면
    if ( $('#posting-box').css('display') == 'block' ) {
			// posting-box를 가리고
      $('#posting-box').hide();
      $("#btn-posting-box").text('포스팅 박스 열기');
    } else {
			// 아니면 posting-box를 펴라
      $('#posting-box').show();
      $("#btn-posting-box").text('포스팅 박스 닫기');

  }    }

  function make_card(){
    //기사 가져오기
    //코멘트 가져오기

    let data = {

        "posting-url":$("#posting-url").val(),
        "posting-comment":$("#posting-comment").val()
        }

    console.log(data);

    $.ajax({
      type: "POST", // POST 방식으로 요청하겠다.
      url: "/post", // /post라는 url에 요청하겠다.
      data: {
        url_give: data["posting-url"],
        comment_give: data["posting-comment"]
        }, // 데이터를 주는 방법
      success: function(result){ // 성공하면
        console.log(result); // 콘솔 창에 결과를 찍어주자
        if(result["result"]=='success'){
                alert("글이 작성되었습니다.")
                 window.location.reload(true);
        }else{
                alert("글 작성에 실패하였습니다.")

        }
      }
    })

//bootstrap grid

//
//  let temp_html = '<div class="card">\
//        <img class="card-img-top" src="https://www.fodors.com/wp-content/uploads/2018/10/4_UltimateRome_PiazzaNavona-975x650.jpg" alt="Card image cap">\
//        <div class="card-body">\
//          <a class="card-title" target="_blank" href="'+data["posting-url"]+'">예를 들면 이렇게 카드가 나옵니다!!</a>\
//          <p class="card-text">여기에 기사 내용이 들어가겠죠</p>\
//          <p class="card-text comment">'+data["posting-comment"]+'</p>\
//        </div>\
//      </div>\
//    </div>';
//
//  console.log(temp_html);
//  $('#cards-box').append(temp_html);
}

