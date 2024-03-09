import './App.css';
import {useState} from 'react';
import axios from 'axios';

function App() {

  const [productName,setProductName] = useState();
  const [data,setData] = useState();
  const [loading, setLoading] = useState(false);
  
  const ProductCard = ({ store, title, price, rating, url }) => {
    return (
      <div className="product-card">
        <h2>{title}</h2>
        <p><strong>Store:</strong> {store}</p>
        <p><strong>Price:</strong> {price}</p>
        <p><strong>Rating:</strong> {rating}</p>
        <a href={url} target="_blank" rel="noopener noreferrer">View on {store}</a>
      </div>
    );
  };
  
  const ProductList = ({ data }) => {
    return (
      <div className="product-list">
        {Object.keys(data).map((key, index) => (
          <ProductCard key={index} {...data[key]} />
        ))}
      </div>
    );
  };

  const handleSearch = async(e) =>{
    e.preventDefault();
    setLoading(true);
    try {
      const url = 'http://127.0.0.1:5000/compare_prices?product='+productName;
      const response = await axios.get(url);
      setData(response.data);
      console.log(response.data);
      setLoading(false);
    } catch (error) {
      console.log(error);
      setLoading(false);
    }
  }
  
  return (
    <div className="App">
      <form onSubmit={handleSearch}>
        <input placeholder="Enter Product Title" value={productName} onChange={(e)=>{setProductName(e.target.value)}}/>
        <button type="submit">Search</button>
      </form>
      {loading && <div>Loading...</div>}
      {data && <ProductList data={data} />}
    </div>
  );
}

export default App;
