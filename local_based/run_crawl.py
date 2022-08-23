from manager.all_manager import All_manager

if __name__=='__main__':
    root_url=input("please enter a root url(string format):")
    q1=int(input("please define the size of url_q:"))
    q2=int(input("please define the size of pagetext_q:"))
    process_n=3
    manager=All_manager(root_url, q1, q2, process_n)
    manager.run()
