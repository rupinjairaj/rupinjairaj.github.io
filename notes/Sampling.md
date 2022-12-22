## Reservior sampling

<code>

	# S has items to sample, R will contain the result
	def ReservoirSample(S[1..n], R[1..k])
  		# fill the reservoir array
  		for i := 1 to k
      		R[i] := S[i]

	# replace elements with gradually decreasing probability
  	for i := k+1 to n
    	# randomInteger(a, b) generates a uniform integer
    	# from the inclusive range {a, ..., b} *)
    	j := randomInteger(1, i)
    	if j <= k
        	R[j] := S[i]

</code>