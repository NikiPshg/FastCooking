import React, { useState, useEffect } from 'react';
import axios from 'axios';

const TextFromServer = () => {
    const [texts, setTexts] = useState([]);

    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/v1/search/')
            .then(response => {
                setTexts(response.data);
            })
            .catch(error => {
                console.error('Ошибка при получении данных:', error);
            });
    }, []);

    return (
        <div>
                {texts.map((item, index) => (
                    <li key={index}>{item.namedish}</li>
                ))}
        </div>
    );
};


export default TextFromServer;