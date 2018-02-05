<template>
    <div  class="container">
        <div class="card border-light mb-12 questionnaire-window">
          <div class="card-body">
            <h5 class="card-title">{{title}}</h5>
            <div class="card-text">
                <div class="card">
                  <div class="card-body">
                      <span v-html="description"></span>
                  </div>
                </div>
                <div class="container-fluid question-container">
                    <div class="row justify-content-md-center">
                        <div class="col-md-8">
                            <div id="alert"></div>
                        </div>
                    </div>
                    <div class="row justify-content-md-center">
                        <div class="col-md-8">
                          <div class="form-group">
                                <label for="exampleFormControlInput1">Email address</label>
                                <input type="email" v-model="email" class="form-control" id="exampleFormControlInput1" placeholder="email">
                          </div>
                        </div>
                    </div>
                    <div class="row justify-content-md-center">
                        <div class="col-md-8">
                            <label>Is this related to climate?</label>
                            <b-form-slider id="range-climate" v-model="score" tooltip="always" :min="-1" :max="1" :step=".1"  :ticks="[-1,0,1]" :ticksPositions="[0,50,100]" :ticksLabels="['Un-Releated','Neither','Related']" :ticksSnapBounds="0"></b-form-slider>
                        </div>
                    </div>
                     <div class="row">
                          <div class="col-md text-center">
                              <button v-on:click="response"  type="button" class=" mb-6 btn btn-lg btn-primary">Submit</button>
                          </div>
                     </div>
                    <div class="row">
                         <div class="col-md text-center">
                            <h6>Abstract read for session: {{count}}</h6>
                         </div>
                    </div>
                </div>
            </div>
          </div>
        </div>
    </div>
</template>

<script>
  import axios from 'axios';
  import $ from 'jquery'
  export default{
      data(){
          return {
              score: 0,
              email:'',
              title: "",
              description: "",
              award_id: 0,
              count: 0
          }
      },
      mounted(){
         this.get_question()
      },
      methods: {
          get_question: function () {
              let self = this
              axios.get('/api/question').then((response) =>{
                  self.award_id = response.data.award_id
                  self.description = response.data.abstract
                  self.title = response.data.title
              })
          },
          response: function () {
               let self = this
              axios.post('/api/response/'+this.award_id,{'email': this.email,'score': this.score}).then((response) => {
                  self.score = 0
                  self.count += 1
                  self.get_question()

              }).catch(function (error) {
                  console.log(error.response.data.err)
                  $('#alert').append('<div class="alert alert-warning alert-dismissible fade show" role="alert">\n' +
                      '  <button type="button" class="close" data-dismiss="alert" aria-label="Close">\n' +
                      '    <span aria-hidden="true">&times;</span>\n' +
                      '  </button>\n' + error.response.data.err +
                      '</div>')
              })
          }
      }

  }
</script>