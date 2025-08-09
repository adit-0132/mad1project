from datetime import datetime
from flask import Flask,render_template,request,url_for,redirect,flash
from .models import *
import matplotlib.pyplot as plot

def routes(app):
    @app.route("/")
    def home():
        #manual admin creation
        #new_user=User_Info(email='admin@myapp.com',password='1234',first_name='adi',last_name='',dob=datetime(2005,3,29,22,33,32),address='address',pincode=110121,contact=1231231230,role=0)
        #db.session.add(new_user)
        #db.session.commit()
        return render_template('index.html')
    
    @app.route("/login",methods=["GET","POST"])
    def signin():
        if request.method=="POST":
            uname=request.form.get("email")
            pwd=request.form.get("password")
            usr=User_Info.query.filter_by(email=uname,password=pwd).first()
            pro=Profs.query.filter_by(email=uname,password=pwd,status="approved").first()
            if usr and usr.role==0:
                return redirect(url_for('admin_dash',name=uname))
            elif usr and usr.role==1:
                return redirect(url_for('user_dash',name=uname))
            elif pro:
                return redirect(url_for('pro_dash',name=uname))
            else:
                return render_template('login.html',msg="Invalid Credentials..")
        return render_template('login.html',msg="" )
    
    @app.route("/admin/<name>")
    def admin_dash(name):
        servReqs= get_servReqs()
        services=get_services()
        profs=get_workprofs()
        pending=pending_profs()
        return render_template('admin_dash.html',name=name,profs=profs,services=services,pendin=pending,ong=servReqs)

    @app.route("/user/<name>")
    def user_dash(name):
        closedReqs=get_closedReqs()
        servReqs= get_servReqs()
        services=get_services()
        return render_template('user_dash.html',bookings=servReqs,closed=closedReqs,services=services,name=name)

    @app.route("/pro/<name>")
    def pro_dash(name):
        id=getproidbyname(name)
        bookings=get_prof_BookingsByID(id)
        return render_template('prof_dash.html',bookings=bookings,name=name)

    @app.route("/signup",methods=["GET","POST"])
    def register():
        if request.method=="POST":
            email=request.form.get("email")
            usr=User_Info.query.filter_by(email=email).first()
            if usr:
                return render_template('customer_signup.html',msg="This email is already registered..")
            pwd=request.form.get("password")
            fname=request.form.get("first_name")
            lname=request.form.get("last_name")
            address=request.form.get("address")
            pincode=request.form.get("pincode")
            contact=request.form.get("contact")
            dobstr=request.form.get("dob")
            try:
                dob = datetime.strptime(dobstr, "%Y-%m-%d").date() 
            except ValueError:
                return "Invalid date format. Please enter a valid date.", 400
            new_user=User_Info(email=email,password=pwd,first_name=fname,last_name=lname,dob=dob,address=address,pincode=pincode,contact=contact,role=1)
            db.session.add(new_user)
            db.session.commit()
            return render_template('login.html',lfg="Registered Successfully, proceed to login..")    
        return render_template('customer_signup.html',lfg="")
    
    @app.route("/prosignup",methods=["GET","POST"])
    def proregister():
        if request.method=="POST":
            email=request.form.get("email")
            usr=Profs.query.filter_by(email=email).first()
            if usr:
                return render_template('professional_signup.html',msg="This email is already registered..")
            pwd=request.form.get("password")
            fname=request.form.get("first_name")
            lname=request.form.get("last_name")
            address=request.form.get("address")
            pincode=request.form.get("pincode")
            doj=datetime.now()
            contact=request.form.get("contact")
            service=request.form.get("service")
            dobstr=request.form.get("dob")
            try:
                dob = datetime.strptime(dobstr, "%Y-%m-%d").date() 
            except ValueError:
                return "Invalid date format. Please enter a valid date.", 400
            new_user=Profs(email=email,password=pwd,first_name=fname,date_joined=doj,last_name=lname,service_type=service,dob=dob,address=address,role=2,pincode=pincode,contact=contact)
            db.session.add(new_user)
            db.session.commit()
            return render_template('login.html')
        services=get_services()
        return render_template('professional_signup.html',services=services)
    
    @app.route("/user/closes/<name>", methods=["GET","POST"])
    def user_closes(name):
        if request.method=="POST":
            booking_id=request.form.get("booking_id")
            action=request.form.get("action")
            booking=Bookings.query.get(booking_id)
            if booking:
                if action=="close":
                    booking.status="closed"
                    db.session.commit()
                return redirect(url_for('user_dash',name=name))
        return redirect(url_for('user_dash', name=name))
            
    @app.route("/user/books/<name>", methods=["GET", "POST"])
    def user_books(name):
        if request.method == "POST":
            service_name = request.form.get("service_name")
            profs=get_profByServ(service_name)
            return render_template('user_books.html',profs=profs,type=service_name,name=name)
        return render_template('user_books.html',name=name)

    @app.route("/user/booking/<name>", methods=["GET", "POST"])
    def user_booking(name):
        if request.method == "POST":
            prof_id = request.form.get("prof_id")
            type=request.form.get("type")
            sid=get_SIDByServ(type)
            uname = request.form.get("user_id")
            uid=get_idbyName(uname)
            action = request.form.get("action")
            if action == "book":
                new_booking = Bookings(
                    date_of_booking=datetime.now(),
                    prof_id=prof_id,
                    service_id=sid,
                    user_id=uid,
                    status="pending")
                db.session.add(new_booking)
                db.session.commit()                
        return redirect(url_for('user_dash', name=name,lfg="Booking Confirmed"))


    @app.route("/admin/professionals/<name>", methods=["GET", "POST"])
    def admin_professionals(name):
        if request.method == "POST":
            action = request.form.get("action")
            prof_id = request.form.get("prof_id")
            professional = Profs.query.get(prof_id)
            if professional:
                if action == "approve":
                    professional.status = "approved"
                elif action == "reject":
                    professional.status = "rejected"
                db.session.commit()
                return redirect(url_for('admin_dash',name=name))
            return render_template('admin_dash.html')
    
    @app.route("/admin/services/<name>", methods=["GET", "POST"])
    def service_modify(name):
        if request.method == "POST":
            action = request.form.get("action")
            service_id = request.form.get("service_id")
            service = Services.query.get(service_id)
            if service:
                if action == "edit":
                    pass
                    #professional.status = "approved"
                elif action == "delete":    
                    try:
                        db.session.delete(service)
                        db.session.commit()  
                    except Exception as e:
                        db.session.rollback()
                return redirect(url_for('admin_dash',name=name))
            return render_template('admin_dash.html')
    
    @app.route("/pro/booking/<name>", methods=["GET", "POST"])
    def booking_confirm(name):
        if request.method == "POST":
            action = request.form.get("action")
            booking_id = request.form.get("booking_id")
            booking = Bookings.query.get(booking_id)
            if booking:
                if action == "Accept":
                    booking.status="ongoing"
                elif action == "Reject":    
                    booking.status="rejected"
                db.session.commit()
                return redirect(url_for('pro_dash',name=name))
            #return render_template('prof_dash.html',name=name)
           
    
    @app.route("/add_service/<name>",methods=["POST","GET"])
    def add_service(name):
        if request.method=="POST":
            sname=request.form.get("name")
            price=request.form.get("price")
            desc=request.form.get("desc")
            new_ser=Services(name=sname,base_price=price,desc=desc)
            db.session.add(new_ser)
            db.session.commit()
            #flash("Service Added Successfully!")
            return redirect(url_for('admin_dash',name=name))
        return render_template('add_service.html',name=name)

#searcher
    @app.route("/admin/search/<name>",methods=["GET","POST"])
    def search(name):
        if request.method=="POST":
            search_text = request.form.get("search_txt").strip()
            results = []
            service_results = Services.query.filter(Services.name.ilike(f"%{search_text}%")).all()
            results.extend(service_results)
            customer_results = Bookings.query.join(User_Info).filter(User_Info.email.ilike(f"%{search_text}%")).all()
            results.extend(customer_results)
            professional_results = Bookings.query.join(Profs).filter(Profs.email.ilike(f"%{search_text}%")).all()
            results.extend(professional_results)
            return render_template("admin_dashboard.html",name=name, search_results=results)
        return redirect(url_for("admin_dashboard",name=name))

#summary functions
    @app.route("/admin_summary")
    def admin_summary():
        plt=get_pro_summary()
        plt.savefig("./static/summary/prof_rating_summary.jpeg")
        plt.clf()
        return render_template("admin_summary.html")

def get_pro_summary():
    pro=get_workprofs()
    summary={}
    for p in pro:
        if p.rating is not None:
            summary[p.email]=p.rating
    x_ids=list(summary.keys())
    y_ratings=list(summary.values())
    plot.bar(x_ids,y_ratings,color="aqua",width=0.5)
    plot.title("Professionals/Ratings")
    plot.xlabel("Professional mails")
    plot.ylabel("Rating")
    return plot

#getter functions
def get_prof_BookingsByID(id):
    bookings=Bookings.query.filter_by(prof_id=id).all()
    return bookings

def getproidbyname(proname):
    pid=Profs.query.filter_by(email=proname).first()
    return pid.id

def get_profByServ(servname):
    profs=Profs.query.filter_by(service_type=servname).all()
    return profs

def get_idbyName(name):
    uid=User_Info.query.filter_by(email=name).first()
    return uid.id

def get_SIDByServ(servname):
    sid=Services.query.filter_by(name=servname).first()
    return sid.service_id

def get_servReqs():
    servReqs=Bookings.query.filter_by(status="ongoing").all()
    return servReqs

def get_closedReqs():
    servReqs=Bookings.query.filter_by(status="closed").all()
    return servReqs

def get_services():
    services=Services.query.all()
    return services

def pending_profs():
    pending_professionals = Profs.query.filter_by(status="pending").all()
    return pending_professionals

def get_workprofs():
    profs=Profs.query.filter_by(status="approved").all()
    return profs