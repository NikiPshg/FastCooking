import React from "react";
import { useLocation } from "react-router-dom";
import "./ml.css";

const MLResultsPage = () => {
  const location = useLocation();
  const { predictionData } = location.state || {};

  if (!predictionData || !predictionData.classes) {
    return <div>Данные предсказания недоступны.</div>;
  }

  return (
    <div className="ml-container">
      <h2>Результат предсказания:</h2>
      <ul className="classes-list">
        {predictionData.classes.map((className, index) => (
          <li key={index} className="class-item">
            {className}
          </li>
        ))}
      </ul>
      <h3>Подходящие рецепты:</h3>
      <div className="recipes-grid">
        {predictionData.matching_recipes.map((recipe, index) => (
          <div key={index} className="recipe-card">
            <h4>{recipe.namedish}</h4>
            <div className="image-container">
              <img
                src={`http://127.0.0.1:8000/media/recipe_images/${recipe.dishid}.jpg`}
                alt={recipe.namedish}
                className="recipe-image"
              />
            </div>
            <p>{recipe.description}</p>
            <p>{recipe.stepdish}</p>
            <h5>Ингредиенты:</h5>
            <ul className="ingredients-list">
              {JSON.parse(recipe.ingr).map((ingredient, index) => (
                <li key={index}>{ingredient}</li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MLResultsPage;
