// test3.cpp : Defines the entry point for the application.
//

#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <iomanip>
using namespace std;
double fRand(double fMin, double fMax)
{
	double f = (double)rand() / RAND_MAX;
	return fMin + f * (fMax - fMin);
}
int main()
{
	string filename("uber-raw-data-sep14.csv");
	ifstream fin;
	string line;
	fin.open(filename);
	string datetitle;
	string lattitle;
	string lontitle;
	string basetitle;
	string IDtitle = "Incident ID";
	string IncidentType = "Incident Type";
	string VideoLink = "Video Link";
	string description = "Description";
	string tempdate;
	string templat;
	string templon;
	string tempbase;
	long long tempID;
	long long IDmax;
	IDmax = 100000000000; //set the upper bound to generate the random number
	vector<string> incidentTypes = { "trip", "too close to heavy equipment" };
	vector<string> videoLinks = { "null", "https://www.youtube.com/watch?v=Goq-yLTafws", "https://www.youtube.com/watch?v=Hm2ZHln_UJY", "https://www.youtube.com/watch?v=ElJbMOEMTk8", "https://www.youtube.com/watch?v=PXUoHeAFtAc", "https://www.youtube.com/watch?v=ydG-lVTq49I", "https://www.youtube.com/watch?v=JOVp5AOUN20"};
	vector<string> descriptions = { "employee has tripped", "empoyee is very close to heavy equipment, safety hazard" };
	vector<string> baseIDS = { "B02512", "B09768", "B06567", "B08798", "B04673", "B05767", "B06376", "B02783", "B04237", "B06788"};
	vector<string> baselatitudes = {"29.07393266320772", "38.83889745592545", "67.28150241774922", "65.76861506352907", "27.850857403798024", "31.400790392869073", "32.14315679366797", "29.7828109", "69.5259183676525", "-38.41968552700519"};
	vector<string> baselongitudes = { "-95.74462745592294", "-90.07362745592292", "8.899795546234275", "7.891749990422023", "-98.58710217513708", "-103.5499547076863", "-102.18566929860735", "-95.618529", "-152.13526519858635", "142.6508871470676"};
	vector<string> basenames = {"Sweeny Refinery", "Wood River Refinery", "SNE-1 well", "Warka well", "Eagle Ford Well", "Permian Basin Well", "Midland Well", "Houston office", "Alphine well", "Otway Basin Well"};
	int videoorno;
	int incidenttypenumber;
	int incidentvideonumber;
	int videonumber;
	int locationnumber;
	string randomdate;
	ofstream myfile;
	myfile.open("data.csv", std::ifstream::trunc);
	srand(time(0));
	int count = 0;
	int tempdatenum;
	if (fin.good()) {
		while (!fin.eof() && count < 100000) {
			if (count == 0) {
				getline(fin, line);
				stringstream string_stream(line);
				cout << line << " " << endl;
				getline(string_stream, datetitle, ',');
				cout << datetitle << endl;
				getline(string_stream, lattitle, ',');
				cout << lattitle << endl;
				getline(string_stream, lontitle, ',');
				cout << lontitle << endl;
				getline(string_stream, basetitle, ',');
				cout << basetitle << endl;
				cout << datetitle << "," << "\"" << IDtitle << "\"" << "," << "\"" << IncidentType << "\"" <<  "," << "\"" << VideoLink << "\"" << "," << "\"" << description << "\"" << "," << lattitle << "," << lontitle << "," << basetitle << endl;
				myfile << datetitle << "," << "\"" << IDtitle << "\"" << "," << "\"" << IncidentType << "\"" << "," << "\"" << VideoLink << "\"" << "," << "\"" << description << "\"" << "," << lattitle << "," << lontitle << "," << "\"" << basetitle << "\"" << endl;
			}
			else {
				tempID = rand() % IDmax + 100000000000000;
				incidenttypenumber = rand() % incidentTypes.size();
				videoorno = rand() % incidentTypes.size();
				if (videoorno == 1) {
					incidentvideonumber = rand() % (videoLinks.size() - 1)/ incidentTypes.size();
					videonumber = incidenttypenumber * (videoLinks.size() - 1) / incidentTypes.size() + incidentvideonumber + 1;
				}
				else {
					incidentvideonumber = 0;
					videonumber = 0;
				}
				locationnumber = rand() % baseIDS.size();

				stringstream ss;
				tempdatenum = rand() % 12 + 1;
				ss << to_string(tempdatenum) + "/";
				tempdatenum = rand() % 28 + 1;
				ss << to_string(tempdatenum) + "/";
				tempdatenum = rand() % 11 + 2010;
				ss << to_string(tempdatenum) + " ";
				tempdatenum = rand() % 12 + 1;
				ss << to_string(tempdatenum) + ":";
				tempdatenum = rand() % 60;
				ss << std::setfill('0') << std::setw(3) << to_string(tempdatenum) + ":";
				tempdatenum = rand() % 60;
				ss << std::setfill('0') << std::setw(3) << to_string(tempdatenum) + " ";
				if (rand() % 2 == 1) {
					ss << "AM";
				}
				else {
					ss << "PM";
				}
				randomdate = ss.str();
				myfile << randomdate << "," << "\"" << tempID << "\"" << "," << "\"" << incidentTypes.at(incidenttypenumber) << "\"" << "," << "\"" << videoLinks.at(videonumber) << "\"" << "," << "\"" << descriptions.at(incidenttypenumber) << " (" << basenames.at(locationnumber) << ")" "\"" << "," << "\"" << to_string(stod(baselatitudes.at(locationnumber)) + fRand(-0.002, 0.002)) << "\"" << "," << "\"" << to_string(stod(baselongitudes.at(locationnumber)) + fRand(-0.0025, 0.0025)) << "\"" << "," << baseIDS.at(locationnumber) << "\"" << endl;
			}
			count++;
		}
	}
	else {
		cout << "bad." << endl;
	}
	myfile.close();
	return 0;
}
