import "./QuoteBlock.css";

// One exact excerpt from the athlete's plan. The component adds the curly
// quotation marks as real characters and never changes the excerpt itself.
export default function QuoteBlock({ quote }) {
  return (
    <blockquote className="quote-block">
      <p className="quote-block__text">{"“"}{quote}{"”"}</p>
    </blockquote>
  );
}
