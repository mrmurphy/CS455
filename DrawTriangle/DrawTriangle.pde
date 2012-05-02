import java.util.Arrays;

//// Point class
class Point implements Comparable{
    public int x;
    public int y;
    public color c;


    public Point(int x, int y){
        this.x = x;
        this.y = y;
        this.c = color(#FFFFFF);

    }
    public Point(int x, int y, color c){
        this.x = x;
        this.y = y;
        this.c = c;

    }

    public boolean biggerX(Point other){
        if (this.x > other.y) return true;
        else return false;
    }
    public boolean biggerY(Point other){
        if (this.y > other.y) return true;
        else return false;
    }

    public int compareTo(Object other) throws ClassCastException {
        if(!(other instanceof Point))
            throw new ClassCastException("A point class is expected here.");
        return (-1 * (this.y - ((Point) other).y));
    }

    public Point minus(Point other){
        int newx = this.x - other.x;
        int newy = this.y - other.y;
        return new Point(newx, newy);
    }
}

class Stepper{
    public int start;
    public int finish;
    public int direction;
    public int val;

    public Stepper(int start, int finish){
        this.start = start;
        this.finish = finish;
        this.val = start;
        if(start < finish){
            this.direction = 1;
        }else{
            this.direction = -1;
        }
    }

    public void step(){
        this.val += this.direction;
    }

    public boolean notDone(){
        if (((this.direction == 1) && (this.val < this.finish)) 
            || ((this.direction == -1) && (this.val >= this.finish))){
            return true;
        }else{
            return false;
        }
    }
}

//// Global variables.
Point[] tri = new Point[3];
int clicks = 0;

//// Code Begin

// Main methods
void setup(){
    size(1000, 1000);
    smooth();
    background(#3E4142);
    noStroke();
}

void mousePressed(){
    if(clicks >= 3) clicks = 0;
    tri[clicks] = new Point(mouseX, mouseY);
    clicks += 1;
}

void draw(){
    background(#3E4142);
    int padding = 25;
    text("Draw three points! ", padding, padding);
    text("Number of clicks: " + clicks, padding, 2*padding);
    markPoint(new Point(mouseX, mouseY));

    for (int i=0; i < clicks; i++) {
        markPoint(tri[i]);
    }

    if(clicks == 3){
        drawTriangle();
    }

}
// Supplementary methods.
void drawTriangle(){
    Arrays.sort(tri);
    Point min = tri[0];
    Point mid = tri[1];
    Point max = tri[2];

        // Work up to the mid point:
    if(!(min.y == mid.y)){
        for (Stepper i = new Stepper(min.y, mid.y); i.notDone(); i.step()) {
            float midx = linearInterp(min, mid, i.val);
            float maxx = linearInterp(min, max, i.val);
            fillScanLine(i.val, midx, maxx);
        }
    }

        // Work from mid to upper:
    if(!(mid.y == max.y)){
        for (Stepper i = new Stepper(mid.y, max.y); i.notDone(); i.step()) {
            float midx = linearInterp(mid, max, i.val);
            float maxx = linearInterp(min, max, i.val);
            fillScanLine(i.val, midx, maxx);
        }
    }
}

void fillScanLine(int yval, float x1, float x2){
    /* Method to fill all x coords at Y between x1 and x2 with a color. */
    for (Stepper i = new Stepper((int)x1, (int)x2); i.notDone(); i.step()) {
        color c = findColor(new Point(i.val, yval));
        set(i.val, yval, c);
    }
}

float linearInterp(Point start, Point end, int cury){
    /* Method to interpolate a value 
    between two known points linearly. */
    int dx = end.x - start.x;
    int dy = end.y - start.y;
    if (dy == 0) dy = 1;
    float curx;

    // This is the equation for linear interpolation.
    curx = (float)start.x + ((float)cury 
        - (float)start.y) * ((float)dx / (float)dy);
    return curx;
}

color findColor(Point p){
    /* Use Barycentric Interpolation to 
    get color of given point within triangle */
    float[] a = new float[3];
    float[] cpercent = new float[3];
    int[] colval = new int[3];
    float atot = getArea(tri[0], tri[1], tri[2]);

    for (int i=0; i<3; i+=1) {
        int j = (i + 1) % 3;
        a[i] = getArea(tri[i], tri[j], p);
        cpercent[i] = (a[i] / atot);
        colval[i] = Math.round(cpercent[i] * 255);
    }

    return color(colval[0], colval[1], colval[2]);
}

float getArea(Point p1, Point p2, Point p3){
    float area = 0;
    Point delA = p1.minus(p2);
    Point delB = p1.minus(p3);

    area = 0.5 * Math.abs(((float)delA.x * (float)delB.y) - 
        ((float)delB.x * (float)delA.y));
    return area;
}

void markPoint(Point p){
    fill(#898F91);
    ellipse(p.x, p.y, 15, 15);
    int offset = 10;
    text(p.x + ", " + p.y, p.x + offset, p.y + offset);
}
