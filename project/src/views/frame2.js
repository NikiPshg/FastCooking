import React from "react";

const MLResultsPage = ({ predictionData }) => {
  return (
    <div>
      <h2>Результат предсказания:</h2>
      <ul>
        {predictionData.classes.map((className, index) => (
          <li key={index}>{className}</li>
        ))}
      </ul>
      <h3>Подходящие рецепты:</h3>
      {predictionData.matching_recipes.map((recipe, index) => (
        <div key={index}>
          <h4>{recipe.namedish}</h4>
          <p>{recipe.description}</p>
          <p>{recipe.stepname}</p>
        </div>
      ))}
    </div>
  );
};

export default MLResultsPage;
