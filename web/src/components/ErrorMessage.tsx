interface Props {
  message: string;
  onGoToStart?: () => void;
}

export function ErrorMessage({ message, onGoToStart }: Props) {
  return (
    <div className="w-full max-w-lg mx-auto text-center py-12">
      <div className="text-5xl mb-4">⚠️</div>
      <h2 className="text-xl font-bold text-gray-700 mb-2">
        エラーが発生しました
      </h2>
      <p className="text-gray-500 mb-6">{message}</p>
      <div className="flex flex-col gap-3 max-w-xs mx-auto">
        {onGoToStart && (
          <button
            onClick={onGoToStart}
            className="px-6 py-3 bg-amber-600 rounded-lg text-white font-bold hover:bg-amber-700 active:scale-[0.98] transition-all"
          >
            条件を変えてやり直す
          </button>
        )}
        <button
          onClick={() => location.reload()}
          className="px-6 py-2 bg-gray-200 rounded-lg text-gray-700 hover:bg-gray-300 transition-colors"
        >
          再読み込み
        </button>
      </div>
    </div>
  );
}
