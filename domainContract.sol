contract mortal { 
    address owner; 
    
    function mortal() { 
        owner = msg.sender; 
    } 
    
    function kill() { 
        if (msg.sender == owner) suicide(owner); 
    } 
} 

contract domainNameTransfer is mortal { 
    enum Status {Init, BuyerSigned, SellerSigned, SellerSetDeal,BuyerPaid,Final}
    struct user{
        string name;
        string email;
        string authenticationProof;
    }
    
    struct domain{
        string domainName; 
        Status status;
        user buyer;
        user seller;
        int price;
        
        string paymentProof;
    }
    
    mapping ( string => domain ) domains;
    
    function domainNameTransfer() public { 
    }
    
    function setDomain(string _domain) public { 
        domains[_domain].domainName = _domain; 
        domains[_domain].buyer=setUser("","");
        domains[_domain].seller=setUser("","");
        domains[_domain].price=0;
        domains[_domain].status=Status.Init;
    } 
    
    function setBuyer(string _domain,string _buyer, string _email) public{
        domains[_domain].buyer=setUser(_buyer,_email);
        domains[_domain].status=Status.BuyerSigned;
    }
    
    function setSeller(string _domain,string _seller, string _email) public{
        domains[_domain].seller=setUser(_seller,_email);
        domains[_domain].status=Status.SellerSigned;
    }
    
    function setUser(string _name, string _email) private returns (user _user){
        _user.name=_name;
        _user.email=_email;
        return _user;
    }
    
    function setDeal(string _domain, int _price) public{
        domains[_domain].price=_price;
        domains[_domain].status=Status.SellerSetDeal;
    }
     
    function setPayment(string _domain,string _paymentProof) public{
        domains[_domain].paymentProof=_paymentProof;
        domains[_domain].status=Status.BuyerPaid;
    }
    
    function finalizeContract(string _domain){
            domains[_domain].status=Status.Final;
    }
    
    function getDomain(string _domain) constant returns (string) {
        return domains[_domain].domainName;
    }
    function getBuyer(string _domain) constant returns (string){
        return domains[_domain].buyer.name;
    }
    function getSeller(string _domain) constant returns (string){
        return domains[_domain].seller.name;
    }
    function getPrice(string _domain) constant returns (int){
        return domains[_domain].price;
    }
    
    function getStatus(string _domain) constant returns (Status){
        return domains[_domain].status;
    }
    
    function getTest() constant returns (string){
        return "HelloWorld";
    }
    
}