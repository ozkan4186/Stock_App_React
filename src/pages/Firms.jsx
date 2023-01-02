import axios from "axios";
import { useEffect } from "react";
import { useSelector } from "react-redux";

const Firms = () => {
  const{token}=useSelector((state)=>state.auth)
    const BASE_URL = "https://14186.fullstack.clarusway.com/";

  const getFirms=async ()=>{

    try {
      const { data } = await axios(`${BASE_URL}stock/firms/ `,{
        headers:{Authorization:`Token ${token}`}
      } );
      console.log(data);
    } catch (error) {
      console.log(error)
    }
  }

useEffect(() => {
  getFirms();

}, []);


  return(
<div>
  

</div>


  ) 
  
};

export default Firms;
