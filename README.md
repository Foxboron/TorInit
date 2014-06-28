TorInit
=======

Helps you generate a sane torrc file.
  
Idea:  
The templates will hold the required values specefied by `options.yaml`.
`options.yaml` will hold teh default configuration, recommendation based on 
template and try achive this in a dynamic way. Leaving little to being hard
coded thus easier to change and keep updated with the current settings 
available in tor.  
  
Further development should also help in generating the script from the terminal
`main.py --template=bridge.template --nick="Hello_World" --ORPort=9001`
