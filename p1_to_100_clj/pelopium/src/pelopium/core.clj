(ns pelopium.core)
(require 'clojure.set)

(defn p1-trigo-v1 []
  (->> (set (range 3 1000 3))
       (clojure.set/union (set (range 5 1000 5)))
       (into [])
       (reduce +)))


(defn muls_of [& muls]
  (fn [start]
    (->> muls
         (map #(- % (mod start %)))
         (reduce min)
         (+ start) )))


(defn p1-trigo-v2 [end]
  (let [muls_of_3_5 (muls_of 3 5)]
    (->> (iterate muls_of_3_5 3)
         (take-while (partial > end))
         (reduce +))))


(defn p2-v1 [accepted? limit]
  (loop [prev 0 fib 1 result 0]
    (if (>= fib limit)
      result
      (recur fib
             (+ fib prev)
             (if (accepted? fib)
               (+ result fib)
               result)))))

(defn jp-iter [f x] (lazy-seq (cons x (jp-iter f (f x)))))

(defn jp-interleave [coll1 coll2]  (apply assoc {} (interleave coll1 coll2)))

(defn jp-juxt [& funcs] (fn [& args] (vec (map #(apply % args) funcs))))