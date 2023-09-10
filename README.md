# <h1><B>catPhish</b></h1><h6><i>an embedded Software to Eliminate Phishing.</i></h6>
<h2>Problem Statement</h2>
<p><h5>Title</h5>
Create an intelligent system using AI/ML to detect phishing domains which imitate look and feel of genuine domains
<h5>Description</h5>
Phishing attack is the most prevalent attack technique to compromise users worldwide. Phishing links/websites are shared through number of mediums like email, SMS etc. to target users. These domains are at times host user login page that imitates the genuine target websites. Login attempts on such pages can lead to compromise of user credentials and may also download malicious payload in user computers. The objective of the problem is to identify such phishing domains from the newly registered websites based on open source databases (Example WHOIS Database). Such databases provide list of newly registered domains. The tool should be automated and harness power of AI/ML to identify phishing domains from genuine domains. It may use the following techniques: (a) Backend code / content similarity in web pages. (b) Web page image analysis (i.e. analysis between genuine and phishing site web page images; more the similarity better is the probability score of being a lookalike phishing site). The evaluation would be based on the toolÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢s ability with regard to the following: (e) Probability scores of phishing domains on how close they are to the genuine domain. (f) Ability to detect new phishing domains in reasonable time. (g) Ease of use and flexibility in output formats.</p><hr>
<p>Organization 	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;National Technical Research Organisation,(NTRO)</p><hr>
<p>Category	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Software</b></p><hr>
<p>Domain &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>Blockchain & Cybersecurity</b></p><hr>
<h1>Table For Accuracy & Pecision Comparison Based on Research Paper's For PHISHING DETECTION</h1>
<p>Accuracy of various ML model used for Phishing detection</p>
<table>
  <tr>
    <th></th>
    <th>Algorithm</th>
    <th>Accuracy</th>
    <th>Precision</th>
    <th>Accuracy_max_ft_3000</th>
   
  </tr>
  <tr>
     <td>0</td>
     <td>KN</td>
     <td>  0.905222 </td>
     <td> 1.000000  </td>
     <td>  0.905222 </td>
  </tr>
   <tr>
     <td>1</td>
     <td>  NB </td>
     <td>  0.978723 </td>
     <td>  1.000000 </td>
     <td> 0.971954</td>
     
  </tr>
   <tr>
     <td>2</td>
     <td> ETC	</td>
     <td>  0.979691  </td>
     <td> 0.991453</td>
     <td>0.979691</td>
   
  </tr>
   <tr>
     <td>3</td>
     <td> RF</td>
     <td> 0.975822 </td>
     <td>0.990826</td>
     <td>0.975822  </td>
    
  </tr>
  <tr>
     <td>4</td>
     <td> SVC</td>
     <td> 0.971954</td>
     <td>  0.974138</td>
     <td> 0.974855</td>
    
  </tr>
   <tr>
     <td>5</td>
     <td> AdaBoost</td>
     <td>0.961315</td>
     <td>0.954128 </td>
     <td> 0.961315</td>
    
  </tr>
   <tr>
     <td>6</td>
     <td> xgb </td>
     <td> 0.968085 </td>
     <td>0.950413</td>
     <td> 0.968085</td>
    
  </tr>
   <tr>
     <td>7</td>
     <td>   LR </td>
     <td> 0.967118 </td>
     <td>0.940000  </td>
     <td> 0.956480</td>
    
  </tr>
  
   <tr>
     <td>8</td>
     <td> GBDT</td>
     <td>  0.946809   </td>
     <td> 0.931373 </td>
     <td>  0.959381</td>
    
  </tr>
   <tr>
     <td>9</td>
     <td>BgC </td>
     <td>0.959381</td>
     <td> 0.861538 </td>
     <td> 0.959381 </td>
    
  </tr>
   <tr>
     <td>10</td>
     <td> DT</td>
     <td>  0.932302</td>
     <td> 0.838095</td>
     <td>0.931335</td>
    
  </tr>
  
 </table>
