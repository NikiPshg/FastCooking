import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ImgFromServer = () => {
    const [articles, setArticles] = useState([]);
    useEffect(() => {
        axios
            .get("http://127.0.0.1:8000/api/v1/urls/")
            .then((response) => {
                setArticles(response.data.image_urls); // Убедитесь, что данные находятся в response.data
                console.log(response.data);
            })
            .catch((error) => {
                console.error("Ошибка при получении данных:", error);
            });

    }, []);

    return (
        <form className="text-form">
            {articles.map((url, index) => (
                <img key={index} src={url} alt={index} className="image"/>
            ))}
        </form>
    );
};

export default ImgFromServer;