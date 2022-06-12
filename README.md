# INeuron-Hacakthon
<b><u>Problem statement Given : </u></b> </br>
<b> Sub Dub [Subtitle and Dubbing]:</b>  Build a software using deep learning to dub a given audio into other languages with the same emotion and pitch. It can be useful as we don’t need a person with knowledge of multiple languages if we could build voice translation. It will be appreciated if one can build near real time voice translation.

<b> We Develop Our Solution using  : </b> <i> <b>`Tacotron 2` </b> :  A neural network architecture for speech synthesis directly from text. </i></br>
 <p> It consists of two components: </p>
 <ol>
<li> a recurrent sequence-to-sequence feature prediction network with attention which predicts a sequence of mel spectrogram frames from an input character sequence </li>
<li> a modified version of WaveNet which generates time-domain waveform samples conditioned on the predicted mel spectrogram frames </li>
  </ol>
  
  <i>Link to understand more on Tacotron : </i> https://github.com/Tomiinek/Multilingual_Text_to_Speech </br>
 <i> Our Project Inspiration link : </i> https://github.com/deterministic-algorithms-lab/Cross-Lingual-Voice-Cloning
  
  <b> Reason to Choose <b>`Tacotron 2` </b> :
  <ul>
    <li>Initially we were planning to use MFCC feature of input audio but then I was difficult to find resource for generate audio to the same audio input language with changing language and as time was a due to planned to go ahead with pretrained model.</li></ul>
  <b> Advantage of Tacotron </b>
  
  <ul> <li> Single Model suppport multilingual text to speech with voice cloning </li></ul>
    <i>Note : Best suited our Problem statement </i>
 
  <b>Our Constructed API :</b> takes `.wav` format audio  file and language in the request body and in response it downloades a zip file of processed audio file as requested with language mentioned . API try to Handles status code such as 200 , 400 , 403 , 500 .
  
  Sample Out for status : 400 
  </br>
   <img src=https://user-images.githubusercontent.com/94001814/173220953-8eda91ab-7806-4fce-b068-8445c1887de0.JPG width=75% height=75%>
   
   Sample Out for status : 500
  </br>
   <img src=https://user-images.githubusercontent.com/94001814/173221292-304dd0b3-3c39-4a18-ada8-d9716efb69da.JPG width=75% height=75%>
   
    Sample Out for status : 200
  </br>
   <img src=https://user-images.githubusercontent.com/94001814/173221533-b0f8c948-9311-4cba-92e9-747441d6a89d.JPG width=75% height=75%>
   
   
   
   
   
   
  
  
  
