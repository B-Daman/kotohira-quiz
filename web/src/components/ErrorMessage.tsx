interface Props {
  message: string;
}

export function ErrorMessage({ message }: Props) {
  return (
    <div className="w-full max-w-lg mx-auto text-center py-12">
      <div className="text-5xl mb-4">⚠️</div>
      <h2 className="text-xl font-bold text-gray-700 mb-2">
        エラーが発生しました
      </h2>
      <p className="text-gray-500">{message}</p>
      <button
        onClick={() => location.reload()}
        className="mt-6 px-6 py-2 bg-gray-200 rounded-lg text-gray-700 hover:bg-gray-300 transition-colors"
      >
        再読み込み
      </button>
    </div>
  );
}
